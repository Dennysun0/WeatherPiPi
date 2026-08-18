import json
import os


'''Vamos a guardar los datos en un JSON'''

#nos guarda la información con el formato ("diccionario") que escribiremos el JSON. DICCIONARIO --> estructura de datos que permite guardar info en forma de CLAVE : VALOR
def guardar_temperatura(dia, minima, maxima):

    archivo_json = "datos/temperaturas.json"

    #esto pregunta: existe la ruta datos/temperaturas.json?? si existe, lo leemos: "r"
    #si nuestro JSON contiene datos, lee todas las entradas del JSON y las convierte en un diccionario Python
    if os.path.exists(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
    else:
        datos = {}  #si nuestro JSON no exite creamos uno

    #[dia] lo que hace es añadir datos dentro de la clave dia
    #ADEMÁS, comprueba si la clave de dicho día existe y así evita duplicidad de datos
    datos[dia] = {      
            "minima": minima,
            "maxima": maxima
    }

    #significa: abre el fichero especificado dentro de la carpeta especificada y crealo si no existe (datos/temperaturas.json); w significa write
    #with se encarga de trabajar de manera segura con los archivos, abre el fichero, ejecuta el codigo que contiene y lo cierra después automáticamente, por eso no necesita un archivo.close()
    with open(archivo_json, "w") as archivo:
        json.dump(datos, archivo, indent=4)     # .dump significa: convierte el "diccionario" datos a JSON, escríbelo en archivo y el indent lo deja bonito
