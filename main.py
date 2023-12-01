# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import database

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    await database.database.connect()

@app.on_event("shutdown")
async def shutdown_db_client():
    await database.database.disconnect()

@app.post("/create")
async def create_item(dispositivo: str, valor: int, db: Session = Depends(database.get_db)):
    return database.create_iot(db, dispositivo, valor)

@app.get("/read/{id}")
async def read_item(id: int, db: Session = Depends(database.get_db)):
    return database.read_iot(db, id)

@app.patch("/update/{id}/{valor}")
async def update_item(id: int, valor: int, db: Session = Depends(database.get_db)):
    return database.update_iot(db, id, valor)

