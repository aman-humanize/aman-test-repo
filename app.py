from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
from fastapi.responses import HTMLResponse

app = FastAPI()

# Simple Bearer token authentication
security = HTTPBearer()

# Hardcoded token for demonstration (replace with secure method in production)
VALID_TOKEN = "supersecrettoken"

def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != VALID_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials.credentials

@app.get("/aman/test")
def aman_test(token: str = Depends(authenticate)):
    return {"message": "Authenticated access to /aman/test!"}

@app.get("/aman/test2")
def aman_test2(token: str = Depends(authenticate)):
    return {"message": "Authenticated access to /aman/test2!"}

@app.get("/aman/test3")
def aman_test3(token: str = Depends(authenticate)):
    return {"message": "Authenticated access to /aman/test3!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/aman/name")
def get_name(token: str = Depends(authenticate)):
    return {"name": "Aman"}

@app.get("/aman/name/html", response_class=HTMLResponse)
def get_name_html():
    return """
    <html>
        <head><title>Name Display</title></head>
        <body>
            <h1>Name: Aman</h1>
        </body>
    </html>
    """
