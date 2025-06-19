# app/main.py

# 1. Importamos FastAPI y las nuevas piezas que creamos
from fastapi import FastAPI
from . import models
from .database import engine

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