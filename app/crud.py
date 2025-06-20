# app/crud.py

from sqlalchemy.orm import Session
from typing import Union, List
from . import models, schemas

def crear_gasto(db: Session, gasto: schemas.GastoCreate) -> models.Gasto:
    """
    Crea un nuevo gasto en la base de datos
    """
    # Crear el objeto Gasto de SQLAlchemy
    # La fecha se asigna automáticamente por el modelo SQLAlchemy
    db_gasto = models.Gasto(
        monto=gasto.monto,
        descripcion=gasto.descripcion,
        categoria=gasto.categoria
    )
    
    # Agregar a la sesión y hacer commit
    db.add(db_gasto)
    db.commit()
    db.refresh(db_gasto)
    
    return db_gasto

def obtener_gastos(db: Session, skip: int = 0, limit: int = 100) -> List[models.Gasto]:
    """
    Obtiene una lista de gastos con paginación opcional
    """
    return db.query(models.Gasto).offset(skip).limit(limit).all()

def obtener_gasto_por_id(db: Session, gasto_id: int) -> Union[models.Gasto, None]:
    """
    Obtiene un gasto específico por su ID
    """
    return db.query(models.Gasto).filter(models.Gasto.id == gasto_id).first() 