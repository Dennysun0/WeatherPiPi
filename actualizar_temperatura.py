from weather import obtener_temperatura
import requests

URL_RASPBERRY = "http://192.168.1.60:8000/temperaturas"

def enviar_temperatura(dia, minima, maxima):
    datos = {
        "dia": dia,
            "mínima": minima,
            "máxima": maxima
    }

    respuesta = requests.post(URL_RASPBERRY, json=datos)

    return respuesta

diaHoy, minima, maxima = obtener_temperatura()

respuesta = enviar_temperatura(diaHoy, minima, maxima)

print(f"Temperatura actualizada: {diaHoy}")
print(f"Mínima: {minima} ºC")
print(f"Máxima: {maxima} ºC")
print(f"Servidor respondió: {respuesta.status_code}")