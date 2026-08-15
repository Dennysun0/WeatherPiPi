from weather import obtener_temperatura

diaHoy, minima, maxima = obtener_temperatura() #A esto se le llama desempaquetado de valores, python reparte automáticamente los valores que devuelve la función

print("Día: ", diaHoy)
print("Temperatura mínima: ", minima, "ºC")
print("Temperatura máxima: ", maxima, "ºC")