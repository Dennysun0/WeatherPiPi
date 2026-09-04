from weather import obtener_temperatura
from storage import guardar_temperatura


diaHoy, minima, maxima = obtener_temperatura()

guardar_temperatura(diaHoy, minima, maxima)

print(f"Temperatura actualizada: {diaHoy}")
print(f"Mínima: {minima} ºC")
print(f"Máxima: {maxima} ºC")
