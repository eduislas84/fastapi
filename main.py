from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Iot

app = FastAPI()

# Configuración para crear y cerrar la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para obtener el valor de un dispositivo
@app.get("/{id}", response_model=dict)
def read_item(id: int, db: Session = Depends(get_db)):
    device = db.query(Iot).filter(Iot.id == id).first()
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return {"id": device.id, "dispositivo": device.dispositivo, "valor": device.valor}

# Endpoint para actualizar el valor de un dispositivo
@app.patch("/{id}/{value}", response_model=dict)
def update_item(id: int, value: int, db: Session = Depends(get_db)):
    device = db.query(Iot).filter(Iot.id == id).first()
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")

    device.valor = value
    db.commit()
    return {"valor": device.valor}
