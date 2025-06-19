# app/database.py

# 1. Importamos las herramientas necesarias de SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 2. Definimos la URL de nuestra base de datos
#    "sqlite:///./test.db" significa que usaremos SQLite y el archivo de
#    la base de datos se llamará "test.db" y estará en la raíz del proyecto.
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# 3. Creamos el "motor" de la base de datos. Es el punto de entrada principal.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 4. Creamos una clase para las sesiones. Esto nos permitirá hablar con la DB.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Creamos una clase "Base". Nuestros modelos de tablas heredarán de ella.
Base = declarative_base()