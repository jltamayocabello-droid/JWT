import jwt 

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyOmlkIjoxLCJpYXQiOjE3OTAwNDMzNDAsIm5iZiI6MTc5MDA0MzM0MCwiZXhwIjoxNzkwMDQ0MjQwfQ.Ap3tsi1GiL-W7wB_yKVosDaH2LWtHsqAaB5mo-sdF_k"

payload = jwt.decode(
    token,
    options={"verify_signature": False}
    )

print("Payload decodificado:",payload)