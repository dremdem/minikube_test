# app.py
import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "ok",
        "version": os.getenv("APP_VERSION", "unknown"),
        "DB_PASSWORD": os.getenv("DB_PASSWORD", "unknown"),
        "API_TOKEN": os.getenv("API_TOKEN", "unknown"),
    }
