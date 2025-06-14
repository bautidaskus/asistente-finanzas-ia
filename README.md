# Asistente de Finanzas con IA 🤖💸

Un asistente inteligente para la gestión de finanzas personales, capaz de procesar gastos a partir de lenguaje natural y categorizarlos automáticamente.

---

## ✨ Descripción del Proyecto

Este proyecto es una API construida con Python y FastAPI que sirve como backend para una aplicación de finanzas. El objetivo principal es permitir a los usuarios registrar sus gastos de una manera intuitiva, simplemente escribiendo una frase. La aplicación utiliza técnicas de Procesamiento de Lenguaje Natural (NLP) para extraer información clave como el monto y el concepto, y asigna una categoría relevante al gasto.

### **Objetivo del MVP (Producto Mínimo Viable)**
La primera versión del proyecto se centra en las siguientes funcionalidades:
-   Registrar un nuevo gasto a través de un endpoint que recibe texto.
-   Extraer el **monto** y el **concepto** del texto.
-   Clasificar el gasto en una categoría predefinida (ej: Alimentos, Transporte, Ocio).
-   Almacenar la información procesada en una base de datos.
-   Ofrecer un endpoint para consultar el listado histórico de gastos.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.10+, FastAPI
* **Base de Datos:** SQLite (para desarrollo), PostgreSQL (para producción)
* **IA / NLP:** spaCy
* **Pruebas:** Pytest
* **Despliegue:** Docker

---

## 🚀 Cómo Ejecutar el Proyecto Localmente

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/bautidaskus/asistente-finanzas-ia.git](https://github.com/bautidaskus/asistente-finanzas-ia.git)
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