from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import engine, SessionLocal
from app.models import models
from app.schemas.schemas import Medicion, MedicionCreate
from app.db import crud

# Esta línea crea físicamente las tablas en la base de datos domovida.db
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="DomoVida API")

# Función para conectar/desconectar de la base de datos de forma segura
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "DomoVida API - Sistema de Salud Activo y Conectado"}

@app.post("/mediciones/", response_model=Medicion)
def crear_nueva_medicion(medicion: MedicionCreate, db: Session = Depends(get_db)):
    return crud.crear_medicion(db=db, medicion=medicion)
@app.get("/mediciones/", response_model=list[Medicion])
def leer_todas_las_mediciones(db: Session = Depends(get_db)):
    mediciones = db.query(models.MedicionSalud).all()
    return mediciones