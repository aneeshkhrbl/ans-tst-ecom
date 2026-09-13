from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    # App Gateway will hit this root path and receive a 200 OK
    return {"status": "Healthy", "component": "HealthProbeContainer"}