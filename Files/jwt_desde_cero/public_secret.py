import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "13468e34634f2d99b4a5cdb0955f7f7684d2609c18ed556bff745498ba5e861e"

now = datetime.now(timezone.utc)

payload = {
    "user_id": 123,
    "username": "pedro",
    "rol": "admin",
    "iat": now,
    "nbf": now,
    "exp": now + timedelta(hours=1)
    
}

token = jwt.encode(
    payload,
    SECRET_KEY,
    algorithm="HS256"
)

print("Token generado:", token)