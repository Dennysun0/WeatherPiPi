from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


#Esta funcion nos dice lo que ocurrirá cuando se utilice /start en el bot, y responderá con el mensaje que tiene
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, soy tu bot de temperaturas.")

#Aquí creamos la aplicación de Telegram utilizando el bot en base al token de bot que le damos
app= Application.builder().token("8868196951:AAFXFWgUG3jWIDvShUKV6SrM4zao0csOk08").build()

#Registramos el comando, que crea la relación entre /start --> start()
app.add_handler(CommandHandler("start", start))

#hace que nuestro programa se quede ejecutándose y pregunte a telegram todo el rato si hay mensajes nuevos
app.run_polling()


