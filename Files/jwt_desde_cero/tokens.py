import jwt 
from datetime import datetime, timedelta, timezone

SECRET_KEY = "Clave_secreta_tokens"
ALGORITHM = "HS256"

now = datetime.now(timezone.utc)

access_token = jwt.encode(
    {
        "sub": "pedro",
        "exp": now + timedelta(minutes=10),
        "iat": now
    },
    SECRET_KEY,
    algorithm=ALGORITHM
)

refresh_token = jwt.encode(
    {
        "sub": "pedro",
        "exp": now + timedelta(days=7),
        "iat": now
    },
    SECRET_KEY,
    algorithm=ALGORITHM
)

print("Acces token generado:", access_token)
print("Refresh token generado:", refresh_token)