from fastapi import FastAPI
from sqlalchemy.orm import Session
from core.database import get_db 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}