import jwt

SECRET_KEY = "clave_secreta"

token = jwt.encode(
    {"user": "pedro"},
    SECRET_KEY,
    algorithm="HS256"
    )

try:
    decoded = jwt.decode(
        token, 
        SECRET_KEY, 
        algorithms=["HS256"]
        )
    print("Firma verificada:", decoded)

except jwt.InvalidTokenError:
    print("Firma no válida")