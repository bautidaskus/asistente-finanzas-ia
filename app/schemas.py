# app/schemas.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Clase base con los campos comunes
class GastoBase(BaseModel):
    monto: float
    descripcion: str
    categoria: Optional[str] = None

# Schema para crear un nuevo gasto (datos de entrada)
class GastoCreate(GastoBase):
    # No necesitamos fecha aquí porque la base de datos la asigna automáticamente
    pass

# Schema para la respuesta de un gasto (datos de salida)
class GastoResponse(GastoBase):
    id: int
    fecha: datetime

    # Configuración para que Pydantic pueda leer desde objetos SQLAlchemy
    class Config:
        from_attributes = True

# Schema para actualizar un gasto (opcional, para futuras funcionalidades)
class GastoUpdate(BaseModel):
    monto: Optional[float] = None
    descripcion: Optional[str] = None
    categoria: Optional[str] = None
    fecha: Optional[datetime] = None 