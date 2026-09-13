import os
import pymssql
from fastapi import FastAPI

app = FastAPI()

def get_db_connection():
    return pymssql.connect(
        server=os.getenv("DB_SERVER"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.get("/health")
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return {"service": "Catalog", "status": "Running", "database": "Connected"}
    except Exception as e:
        return {"service": "Catalog", "status": "Running", "database": f"Failed to connect: {str(e)}"}