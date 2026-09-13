# ordering.py
from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health(): return {"service": "Ordering", "status": "Running"}