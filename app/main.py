# app/main.py

# 1. Importamos FastAPI y las nuevas piezas que creamos
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, crud
from .database import engine, get_db

# 2. Esta es la línea mágica que crea la base de datos y la tabla
#    Le dice a SQLAlchemy: "Mira todos los modelos que heredan de Base
#    (como nuestra clase Gasto) y créalos como tablas en la base de datos".
#    Esto solo se ejecuta si la tabla no existe previamente.
models.Base.metadata.create_all(bind=engine)

# 3. El resto de la configuración de la app
app = FastAPI(
    title="Asistente de Finanzas con IA",
    description="Una API para procesar y gestionar gastos personales mediante NLP.",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {"message": "¡Hola! Bienvenido a la API del Asistente de Finanzas."}

@app.post("/gastos/", response_model=schemas.GastoResponse, status_code=201)
def crear_gasto(gasto: schemas.GastoCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo gasto en la base de datos.
    
    - **monto**: El monto del gasto (requerido)
    - **descripcion**: Descripción del gasto (requerido)
    - **categoria**: Categoría del gasto (opcional)
    
    La fecha se asigna automáticamente al momento de la creación.
    """
    return crud.crear_gasto(db=db, gasto=gasto)

@app.get("/gastos/", response_model=List[schemas.GastoResponse])
def obtener_gastos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Obtiene la lista de todos los gastos con paginación opcional.
    
    - **skip**: Número de registros a saltar (para paginación)
    - **limit**: Número máximo de registros a devolver
    """
    gastos = crud.obtener_gastos(db, skip=skip, limit=limit)
    return gastos

@app.get("/gastos/{gasto_id}", response_model=schemas.GastoResponse)
def obtener_gasto(gasto_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un gasto específico por su ID.
    
    - **gasto_id**: El ID del gasto a buscar
    """
    gasto = crud.obtener_gasto_por_id(db, gasto_id=gasto_id)
    if gasto is None:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")
    return gasto