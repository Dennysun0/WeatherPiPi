import requests

#creamos nuestra función

def obtener_temperatura():
    latitud = 42.00955
    longitud = -4.52406

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitud}"
        f"&longitude={longitud}"
        "&daily=temperature_2m_min,temperature_2m_max"  #esto dice que quiere los datos diarios de max y min
        "&timezone=Europe/Madrid"   #los datos se interpreten en esta zona horaria
    )

    #contruimos la petición http (GET) --> Open-Meteo --> JSON respueta
    respuesta = requests.get(url)

    #print(respuesta.json()) #convertimos la respueta a Python, ya no hace falta


    '''Vamos a visualizar los datos del JSON, solo el primer día [0] que es es actual'''

    datos = respuesta.json()

    diaHoy = datos["daily"]["time"][0]
    minima = datos["daily"]["temperature_2m_min"][0]
    maxima = datos["daily"]["temperature_2m_max"][0]

    return diaHoy, minima, maxima