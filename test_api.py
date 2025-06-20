# test_api.py
# Script simple para probar la API

import requests
import json

# URL base de la API
BASE_URL = "http://127.0.0.1:8000"

def test_crear_gasto():
    """Prueba crear un nuevo gasto"""
    print("🧪 Probando crear un gasto...")
    
    # Datos del gasto a crear
    gasto_data = {
        "monto": 1500.50,
        "descripcion": "Compra en supermercado",
        "categoria": "Alimentos"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/gastos/", json=gasto_data)
        
        if response.status_code == 201:
            gasto_creado = response.json()
            print(f"✅ Gasto creado exitosamente!")
            print(f"   ID: {gasto_creado['id']}")
            print(f"   Monto: ${gasto_creado['monto']}")
            print(f"   Descripción: {gasto_creado['descripcion']}")
            print(f"   Categoría: {gasto_creado['categoria']}")
            print(f"   Fecha: {gasto_creado['fecha']}")
            return gasto_creado['id']
        else:
            print(f"❌ Error al crear gasto: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("❌ No se pudo conectar a la API. Asegúrate de que el servidor esté ejecutándose.")
        return None

def test_obtener_gastos():
    """Prueba obtener la lista de gastos"""
    print("\n🧪 Probando obtener lista de gastos...")
    
    try:
        response = requests.get(f"{BASE_URL}/gastos/")
        
        if response.status_code == 200:
            gastos = response.json()
            print(f"✅ Se obtuvieron {len(gastos)} gastos:")
            
            for gasto in gastos:
                print(f"   - ID: {gasto['id']}, ${gasto['monto']} - {gasto['descripcion']}")
        else:
            print(f"❌ Error al obtener gastos: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ No se pudo conectar a la API.")

def test_obtener_gasto_por_id(gasto_id):
    """Prueba obtener un gasto específico por ID"""
    print(f"\n🧪 Probando obtener gasto con ID {gasto_id}...")
    
    try:
        response = requests.get(f"{BASE_URL}/gastos/{gasto_id}")
        
        if response.status_code == 200:
            gasto = response.json()
            print(f"✅ Gasto encontrado:")
            print(f"   ID: {gasto['id']}")
            print(f"   Monto: ${gasto['monto']}")
            print(f"   Descripción: {gasto['descripcion']}")
            print(f"   Categoría: {gasto['categoria']}")
            print(f"   Fecha: {gasto['fecha']}")
        else:
            print(f"❌ Error al obtener gasto: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ No se pudo conectar a la API.")

if __name__ == "__main__":
    print("🚀 Iniciando pruebas de la API...")
    print("=" * 50)
    
    # Probar crear un gasto
    gasto_id = test_crear_gasto()
    
    # Probar obtener todos los gastos
    test_obtener_gastos()
    
    # Probar obtener un gasto específico
    if gasto_id:
        test_obtener_gasto_por_id(gasto_id)
    
    print("\n" + "=" * 50)
    print("🏁 Pruebas completadas!") 