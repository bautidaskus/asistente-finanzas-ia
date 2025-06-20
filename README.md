# Asistente de Finanzas con IA 🤖💸

Un asistente inteligente para la gestión de finanzas personales, capaz de procesar gastos a partir de lenguaje natural y categorizarlos automáticamente.

---

## ✨ Descripción del Proyecto

Este proyecto es una API construida con Python y FastAPI que sirve como backend para una aplicación de finanzas. El objetivo principal es permitir a los usuarios registrar sus gastos de una manera intuitiva, simplemente escribiendo una frase. La aplicación utiliza técnicas de Procesamiento de Lenguaje Natural (NLP) para extraer información clave como el monto y el concepto, y asigna una categoría relevante al gasto.

### **Objetivo del MVP (Producto Mínimo Viable)**
La primera versión del proyecto se centra en las siguientes funcionalidades:
-   ✅ Registrar un nuevo gasto a través de un endpoint que recibe texto.
-   ✅ Extraer el **monto** y el **concepto** del texto.
-   ✅ Clasificar el gasto en una categoría predefinida (ej: Alimentos, Transporte, Ocio).
-   ✅ Almacenar la información procesada en una base de datos.
-   ✅ Ofrecer un endpoint para consultar el listado histórico de gastos.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.10+, FastAPI
* **Base de Datos:** SQLite (para desarrollo), PostgreSQL (para producción)
* **ORM:** SQLAlchemy
* **Validación de Datos:** Pydantic
* **IA / NLP:** spaCy (próximamente)
* **Pruebas:** Pytest
* **Despliegue:** Docker

---

## 🚀 Cómo Ejecutar el Proyecto Localmente

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/bautidaskus/asistente-finanzas-ia.git
    cd asistente-finanzas-ia
    ```

2.  **Crear y activar el entorno virtual:**
    ```bash
    py -m venv venv
    venv\Scripts\activate
    ```

3.  **Instalar las dependencias:**
    ```bash
    py -m pip install -r requirements.txt
    ```

4.  **Ejecutar el servidor de desarrollo:**
    ```bash
    uvicorn app.main:app --reload
    ```

5.  Abrir el navegador en `http://127.0.0.1:8000`.

---

## 📚 Documentación de la API

Una vez que el servidor esté ejecutándose, puedes acceder a:
- **Documentación automática:** `http://127.0.0.1:8000/docs`
- **Documentación alternativa:** `http://127.0.0.1:8000/redoc`

### Endpoints Disponibles

#### `POST /gastos/`
Crea un nuevo gasto en la base de datos.

**Datos requeridos:**
```json
{
    "monto": 1500.50,
    "descripcion": "Compra en supermercado",
    "categoria": "Alimentos"
}
```

**Respuesta:**
```json
{
    "id": 1,
    "monto": 1500.50,
    "descripcion": "Compra en supermercado",
    "categoria": "Alimentos",
    "fecha": "2024-01-15T10:30:00"
}
```

#### `GET /gastos/`
Obtiene la lista de todos los gastos con paginación opcional.

**Parámetros opcionales:**
- `skip`: Número de registros a saltar (para paginación)
- `limit`: Número máximo de registros a devolver (máximo 100)

#### `GET /gastos/{gasto_id}`
Obtiene un gasto específico por su ID.

---

## 🧪 Probando la API

Puedes probar la API de varias maneras:

### 1. Usando el script de prueba incluido:
```bash
python test_api.py
```

### 2. Usando curl:
```bash
# Crear un gasto
curl -X POST "http://127.0.0.1:8000/gastos/" \
     -H "Content-Type: application/json" \
     -d '{"monto": 1500.50, "descripcion": "Compra en supermercado", "categoria": "Alimentos"}'

# Obtener todos los gastos
curl -X GET "http://127.0.0.1:8000/gastos/"

# Obtener un gasto específico
curl -X GET "http://127.0.0.1:8000/gastos/1"
```

### 3. Usando la documentación interactiva:
Ve a `http://127.0.0.1:8000/docs` y prueba los endpoints directamente desde el navegador.

---

## 📁 Estructura del Proyecto

```
asistente-finanzas-ia/
├── app/
│   ├── __init__.py
│   ├── main.py          # Configuración de FastAPI y endpoints
│   ├── models.py        # Modelos de SQLAlchemy
│   ├── schemas.py       # Schemas de Pydantic
│   ├── crud.py          # Operaciones de base de datos
│   └── database.py      # Configuración de la base de datos
├── tests/               # Pruebas unitarias
├── requirements.txt     # Dependencias del proyecto
├── test_api.py         # Script de prueba de la API
└── README.md           # Este archivo
```

---

## 🔄 Próximos Pasos

- [ ] Implementar procesamiento de lenguaje natural (NLP)
- [ ] Agregar categorización automática de gastos
- [ ] Implementar análisis y reportes financieros
- [ ] Agregar autenticación de usuarios
- [ ] Crear interfaz web