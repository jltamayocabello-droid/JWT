import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "clase_secreta_refresh"

now = datetime.now(timezone.utc)

payload = {
    "user_id": 1,
    "type": "refresh",
    "iat": now,
    "nbf": now,
    "exp": now + timedelta(days=7)
}

refresh_token = jwt.encode(
    payload,
    SECRET_KEY,
    algorithm="HS256"
)

print("Refresh token generado:", refresh_token)