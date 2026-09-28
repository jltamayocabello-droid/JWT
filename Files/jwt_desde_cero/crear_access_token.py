import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "clase_secreta_del_servidor"

now = datetime.now(timezone.utc)

payload = {
    "user_id": 1,
    "iat": now,
    "nbf": now,
    "exp": now + timedelta(minutes=10)
}

acces_token = jwt.encode(
    payload,
    SECRET_KEY,
    algorithm="HS256"
)

print("Acces token generado:", acces_token)