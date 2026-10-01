from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
import jwt 

app = FastAPI()

SECRET_KEY = "mi_clave_super_secreta"
ALGORITHM = "HS256"

class RefreshToken(BaseModel):
    refresh_token: str

@app.post("/refresh")
def refresh(data: RefreshToken):
    try:
        payload = jwt.decode(
            data.refresh_token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")

    now = datetime.now(timezone.utc)

    new_access_token = jwt.encode(
        {
            "sub": payload["sub"],
            "exp": now + timedelta(minutes=10)
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {"access_token": new_access_token}

 