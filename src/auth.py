from fastapi import FastAPI

app = FastAPI()

@app.get("/auth")
def login_page():
    return {"message": "Authentication service is running. Login UI coming soon."}