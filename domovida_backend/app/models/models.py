from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.database import Base

class MedicionSalud(Base):
    __tablename__ = "mediciones"

    id = Column(Integer, primary_key=True, index=True)
    usuario_nombre = Column(String)
    ritmo_cardiaco = Column(Float)
    oxigeno_sangre = Column(Float)
    fecha_registro = Column(DateTime, default=datetime.utcnow)