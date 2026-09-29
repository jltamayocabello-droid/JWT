import jwt 
from datetime import datetime, timedelta, timezone
import time

SECRET_KEY = "mi_clave_super_secreta"
now = datetime.now(timezone.utc)

token = jwt.encode(
    {
        "user": "pedro",
        "exp": now + timedelta(seconds=3)
    },
    SECRET_KEY,
    algorithm="HS256"
)

print("Token generado:", token)

time.sleep(5)

try:
    jwt.decode(
        token,
        SECRET_KEY,
        algorithms=["HS256"]
    )
    print("Firma válida")

except jwt.ExpiredSignatureError:
    print("Firma expirada")