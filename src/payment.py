# payment.py
from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health(): return {"service": "Payment", "status": "Running"}