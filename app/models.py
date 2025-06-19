# app/models.py

# 1. Importamos las herramientas para definir columnas y tipos de datos
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

# 2. Importamos nuestra clase Base desde el archivo database.py
from .database import Base

# 3. Creamos una clase que representa nuestra tabla "gastos"
class Gasto(Base):
    # Este es el nombre que tendrá la tabla en la base de datos real
    __tablename__ = "gastos"

    # Aquí definimos cada columna con su tipo de dato y propiedades
    id = Column(Integer, primary_key=True, index=True) # Clave primaria única
    monto = Column(Float, nullable=False) # No puede estar vacío
    descripcion = Column(String, index=True)
    fecha = Column(DateTime, default=datetime.utcnow) # Se pone la fecha/hora actual por defecto
    categoria = Column(String, index=True)