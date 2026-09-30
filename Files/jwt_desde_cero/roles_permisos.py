from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

SECRET_KEY = "mi_clave_super_secreta"
ALGORITHM = "HS256"

class LoginRequest(BaseModel):
    username: str
    password: str

fake_users_db = {
    "admin": {
        "password": "1234",
        "rol": "admin",
        "scopes": ["users:read", "users:write", "reports:vies"]
    },
    "qa": {
        "password": "1234",
        "rol": "qa",
        "scopes": ["reports:view"]
    },
    "user": {
        "password": "1234",
        "rol": "user",
        "scopes": []
    }
}

def create_jwt_token(user_data: dict, username: str) -> str:
    expiration_time = datetime.now(timezone.utc) + timedelta(hours=1)
    now = datetime.now(timezone.utc)

    payload = {
        "sub": username,
        "role": user_data["role"],
        "scopes": user_data["scopes"],
        "iat": now,
        "nbf": now,
        "exp": now + timedelta(minutes=20)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return token

@app.post("/login")
def login(request: LoginRequest):
    user = fake_users_db.get(request.username)

    if not user or user["password"] != request.password:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    token = create_jwt_token(user, request.username)
    return {
        "access_token": token,
        "token_type": "bearer"
    }

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")

    return payload

def require_role(required_roles: list):
    def role_checker(user=Depends(get_current_user)):
        if user["role"] not in required_roles:
            raise HTTPException(status_code=403, detail="Acceso denegado")
        return user
    return role_checker

def require_scope(required_scopes: str):
    def scope_checker(user=Depends(get_current_user)):
        if required_scopes not in user["scopes"]:
            raise HTTPException(status_code=403, detail="Acceso denegado")
        return user
    return scope_checker

@app.get("/admin-area")
def admin_endpoint(user=Depends(require_role(["admin"]))):
    return {"message": "Acceso concedido"}

@app.get("/reports")
def reports_endpoint(user=Depends(require_scope("reports:view"))):
    return {"message": "Acceso concedido"}

    