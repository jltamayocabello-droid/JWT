from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

def simple_guard():
    allowed = True
    if not allowed:
        raise HTTPException(status_code=403, detail="Acceso denegado")
    return

@app.get("/protected")
def protected_endpoint(dep=Depends(simple_guard)):
    return {"message": "Acceso concedido"}