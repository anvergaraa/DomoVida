from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas

def crear_medicion(db: Session, medicion: schemas.MedicionCreate):
    db_medicion = models.MedicionSalud(
        usuario_nombre=medicion.usuario_nombre,
        ritmo_cardiaco=medicion.ritmo_cardiaco,
        oxigeno_sangre=medicion.oxigeno_sangre
    )
    db.add(db_medicion)
    db.commit()
    db.refresh(db_medicion)
    return db_medicion