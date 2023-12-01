from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
import database

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para obtener un valor por ID
@app.get("/{id}")
def read_item(id: int, db: Session = Depends(get_db)):
    item = db.query(database.IoT).filter(database.IoT.id == id).first()
    if item:
        return {"id": item.id, "dispositivo": item.dispositivo, "valor": item.valor}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# Endpoint para actualizar un valor por ID
@app.patch("/{id}/{value}")
def update_item(id: int, value: int, db: Session = Depends(get_db)):
    item = db.query(database.IoT).filter(database.IoT.id == id).first()
    if item:
        item.valor = value
        db.commit()
        return {"id": item.id, "dispositivo": item.dispositivo, "valor": item.valor}
    else:
        raise HTTPException(status_code=404, detail="Item not found")