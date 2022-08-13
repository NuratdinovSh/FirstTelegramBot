from email import message
from turtle import up
from webbrowser import get
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Russian🇷🇺", callback_data="Russian"),
            InlineKeyboardButton("English🇺🇸", callback_data="English")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Hello, choose your language", reply_markup=reply_markup)

async def getPhoto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Nice photo")

async def getMessage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    if message == "Russian🇷🇺" or message == "Русский🇷🇺":
        q1 = KeyboardButton("Что ты делаешь?")
        q2 = KeyboardButton("Как ты?")
        q3 = KeyboardButton("Где ты?")
        q4 = KeyboardButton('Как тебя зовут?')
        menu = KeyboardButton("Меню")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[q1, q2, q3], [q4], [menu]], resize_keyboard=True)
        await update.message.reply_text(text="Задайте эти вопросы боту", reply_markup=replymarkup)
    elif message == "Меню":
        rubutton = KeyboardButton(text="Русский🇷🇺")
        engbutton = KeyboardButton(text="Английский🇺🇸")
        replymarkup = ReplyKeyboardMarkup(keyboard= [[rubutton, engbutton]], resize_keyboard=True)
        await update.message.reply_text(text="Выберите свой язык", reply_markup=replymarkup)
    elif message == "English🇺🇸" or message == "Английский🇺🇸":
        q1 = KeyboardButton("What are you doing?")
        q2 = KeyboardButton("How are you?")
        q3 = KeyboardButton("Where are you?")
        q4 = KeyboardButton("What is your name?")
        menu = KeyboardButton("Menu")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[q1, q2, q3], [q4], [menu]], resize_keyboard=True)
        await update.message.reply_text(text="Ask these questions to the bot", reply_markup=replymarkup)
    elif message == "Menu":
        rubutton = KeyboardButton(text="Russian🇷🇺")
        engbutton = KeyboardButton(text="English🇺🇸")
        replymarkup = ReplyKeyboardMarkup(keyboard= [[rubutton, engbutton]], resize_keyboard=True)
        await update.message.reply_text(text="Choose your language", reply_markup=replymarkup)
    elif message == "What are you doing?":
        await update.message.reply_text("Nothing")
    elif message == "How are you?":
        await update.message.reply_text("I am fine")
    elif message == "Where are you?":
        await update.message.reply_text("In your phone")               
    elif message == "Что ты делаешь?":
        await update.message.reply_text("Ничего")
    elif message == "What is your name?":
        await update.message.reply_text("Sharapatdin's bot")
    elif message == "Как ты?":
        await update.message.reply_text("Хорошо")
    elif message == "Где ты?":
        await update.message.reply_text("В твоём телефоне")
    elif message == "Как тебя зовут?":
        await update.message.reply_text("Sharapatdin's bot") 
    else:
        await update.message.reply_text("wrong question")



if __name__ == '__main__':
    application = ApplicationBuilder().token('5536219218:AAHrE4bI1fxDlD88TxWNGv6_oqb-gl5DFRw').build()
    
    start_handler = CommandHandler('start', start)
    photo_handler = MessageHandler(filters.PHOTO, getPhoto)
    message_handler = MessageHandler(filters.TEXT, getMessage)

    application.add_handler(start_handler)
    application.add_handler(photo_handler)
    application.add_handler(message_handler)
    

    application.run_polling()