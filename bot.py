from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from weather import obtener_temperatura
import requests

URL_RASPBERRY = "http://192.168.1.196:8000/temperaturas"


'''Función para /start'''

#Esta funcion nos dice lo que ocurrirá cuando se utilice /start en el bot, y responderá con el mensaje que tiene
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, soy tu bot de temperaturas.")



'''
    Definamos ahora la función para obtener la temperatura en el bot y enviarla al servidor
        Ahora añadimos la función guardar_temperatura()
        Añadimos la funcionalidad de enviar la temperatura mediante la petición HTTP POST
'''

async def temperatura(update: Update, context: ContextTypes.DEFAULT_TYPE):
    diaHoy, minima, maxima = obtener_temperatura()

    enviar_temperatura(diaHoy, minima, maxima)

    await update.message.reply_text(
        f"Temperatura de hoy en Palencia\n\n"
        f" Día: {diaHoy}\n"             #f" " son f-strings, que permiten introducir variables dentro de una cadena
        f" Mínima: {minima} ºC\n"
        f" Máxima: {maxima} ºC"
    )


''' Función para enviar la temperatura
    la usaremos dentro de temperatura para que se
    llame a la hora de usar /temperatura en el bot
'''

def enviar_temperatura(dia, minima, maxima):
    datos = {
    "dia": dia,
    "minima": minima,
    "maxima": maxima
    }

    respuesta = requests.post(URL_RASPBERRY, json=datos)

    return respuesta

#Aquí creamos la aplicación de Telegram utilizando el bot en base al token de bot que le damos
app= Application.builder().token("8868196951:AAFZIQcGVo-jloEluZhHPN70Kg5m0H6HmFo").build()


#Registramos el comando, que crea la relación entre /start --> start()
app.add_handler(CommandHandler("start", start))
#Registramos el comando para /temperatura
app.add_handler(CommandHandler("temperatura", temperatura))


#hace que nuestro programa se quede ejecutándose y pregunte a telegram todo el rato si hay mensajes nuevos
app.run_polling()


