from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from weather import obtener_temperatura
from storage import guardar_temperatura





'''Función para /start'''

#Esta funcion nos dice lo que ocurrirá cuando se utilice /start en el bot, y responderá con el mensaje que tiene
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, soy tu bot de temperaturas.")



'''Definamos ahora la función para obtener la temperatura en el bot'''

async def temperatura(update: Update, context: ContextTypes.DEFAULT_TYPE):
    diaHoy, minima, maxima = obtener_temperatura()

    await update.message.reply_text(
        f" Día: {diaHoy}\n"             #f" " son f-strings, que permiten introducir variables dentro de una cadena
        f" Mínima: {minima} ºC\n"
        f" Máxima: {maxima} ºC"
    )


#Aquí creamos la aplicación de Telegram utilizando el bot en base al token de bot que le damos
app= Application.builder().token("8868196951:AAFXFWgUG3jWIDvShUKV6SrM4zao0csOk08").build()


#Registramos el comando, que crea la relación entre /start --> start()
app.add_handler(CommandHandler("start", start))
#Registramos el comando para /temperatura
app.add_handler(CommandHandler("temperatura", temperatura))


#hace que nuestro programa se quede ejecutándose y pregunte a telegram todo el rato si hay mensajes nuevos
app.run_polling()


