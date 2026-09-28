from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

SECRET_KEY = "mi_clave_super_secreta"
ALGORITHM = "HS256"

class LoginRequest(BaseModel):
    username: str
    password: str

faker_user_db = {
        "Carlos": {
            "username": "Carlos",
            "password": "1234",
            "rol": "admin"
        }
    }

def create_jwt_token(user_data:dict) -> str:
       now = datetime.now(timezone.utc)

       payload = {
           "sub": user_data["username"],
           "rol": user_data["rol"],
           "iat": now,
           "nbf": now,
           "exp": now + timedelta(minutes=17)
       }
       token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

       return token

@app.post("/login")
def login(request: LoginRequest):
    user = faker_user_db.get(request.username)
    if not user or user["password"] != request.password:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    token = create_jwt_token(user)
    return {
        "access_token": token,
        "token_type": "bearer"
            }