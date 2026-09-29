payload = {
    "sub": "carlos",
    "role": "admin"
}

username = payload.get("sub")
role = payload.get("role")

if not username or not role:
    print("Payload no válido, faltan datos")

else:
    print("Username:", username)
    print("Role:", role)