from pydantic import BaseModel

# Este es el "molde" básico para tus datos de salud
class MedicionBase(BaseModel):
    usuario_nombre: str
    ritmo_cardiaco: float
    oxigeno_sangre: float

# Este se usa para cuando creas una nueva medición
class MedicionCreate(MedicionBase):
    pass

# Este es el que devuelve el sistema con el ID que asigna la base de datos
class Medicion(MedicionBase):
    id: int

    class Config:
        from_attributes = True