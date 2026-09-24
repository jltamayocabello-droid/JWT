import jwt 
from jwt import InvalidTokenError

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyOmlkIjoxLCJpYXQiOjE3OTAwNDMzNDAsIm5iZiI6MTc5MDA0MzM0MCwiZXhwIjoxNzkwMDQ0MjQwfQ.Ap3tsi1GiL-W7wB_yKVosDaH2LWtHsqAaB5mo-sdF_k"

SECRET_KEY = "mi_clave_super_secreta"

try:
    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    print("Firma verificada:", decoded)

except InvalidTokenError:
    print("Firma no válida")