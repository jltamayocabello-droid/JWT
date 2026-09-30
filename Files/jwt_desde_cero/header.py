auth_header = "Bearer abc.def.ghi"

prefix, token = auth_header.split(" ")

print("Prefix:", prefix)
print("Token:", token)