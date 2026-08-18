import requests

print("Iniciando prueba")

url = "http://192.168.1.196:8000/temperatura"

datos = {
    "dia": "2026-08-18",
    "minima": 18.5,
    "maxima": 31.2
}

respuesta = requests.post(url, json=datos)

print("Respuesta del servidor:")
print(respuesta.text)