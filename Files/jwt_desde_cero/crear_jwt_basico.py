import jwt
from datetime import datetime, timezone

SECRET_KEY = "clave_secreta_del_servidor"

now = datetime.now(timezone.utc)

payload = {
    "iat" : now
}

token = jwt.encode(
    payload,
    SECRET_KEY,
    algorithm="HS256"
)

print("JWT generado:", token)