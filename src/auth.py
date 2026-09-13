# auth.py
from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health(): return {"service": "Auth", "status": "Running"}