import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "mi_clave_super_secreta"
now = datetime.now(timezone.utc)

patyload = {
    "user:id": 1,
    "iat" : now,
    "nbf" : now,
    "exp" : now + timedelta(minutes=15)
}

token = jwt.encode(
    patyload, 
    SECRET_KEY, 
    algorithm="HS256"
    )

print("JWT generado:", token)