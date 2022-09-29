from ast import Call
from email import message
from turtle import up
from webbrowser import get
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler

calkulatorKeyboard = [
            [
                InlineKeyboardButton("C", callback_data="C"),
                InlineKeyboardButton("/", callback_data="/"),
                InlineKeyboardButton("*", callback_data="*"),
                InlineKeyboardButton("-", callback_data="-")
            ],
            [
                InlineKeyboardButton("7", callback_data="7"),
                InlineKeyboardButton("8", callback_data="8"),
                InlineKeyboardButton("9", callback_data="9"),
                InlineKeyboardButton("+", callback_data="+")
            ],
            [
                InlineKeyboardButton("4", callback_data="4"),
                InlineKeyboardButton("5", callback_data="5"),
                InlineKeyboardButton("6", callback_data="6"),
                InlineKeyboardButton(",", callback_data=",")
            ],
            [
                InlineKeyboardButton("1", callback_data="1"),
                InlineKeyboardButton("2", callback_data="2"),
                InlineKeyboardButton("3", callback_data="3"),
                InlineKeyboardButton("=", callback_data="=")
            ],
            [
                InlineKeyboardButton(" ", callback_data=" "),
                InlineKeyboardButton("0", callback_data="0"),
                InlineKeyboardButton(" ", callback_data=" "),
                InlineKeyboardButton(" ", callback_data=" ")
            ]
        ]
async def startCallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Russian🇷🇺", callback_data="Russian"),
            InlineKeyboardButton("English🇺🇸", callback_data="English")
        ]
    ]

    replymarkup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Hello, choose your language", reply_markup=replymarkup)

async def inlineButtonCallback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    message = update.callback_query.message.text

    await query.answer()

    if query.data == "Russian":
        q1 = KeyboardButton("Что ты делаешь?")
        q2 = KeyboardButton("Как вы?")
        q3 = KeyboardButton("Где ты?")
        q4 = KeyboardButton('Как тебя зовут?')
        q5 = KeyboardButton("Сколько тебе лет?")
        menu = KeyboardButton("Меню")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[q1, q2, q3], [q4, q5], [menu]], resize_keyboard=True)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Задайте эти вопросы боту", reply_markup=replymarkup)
    elif query.data == "English":
        q1 = KeyboardButton("What are you doing?")
        q2 = KeyboardButton("How are you?")
        q3 = KeyboardButton("Where are you?")
        q4 = KeyboardButton("What is your name?")
        q5 = KeyboardButton("How old are you?")
        menu = KeyboardButton("Menu")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[q1, q2, q3], [q4, q5], [menu]], resize_keyboard=True)
        #await update.message.reply_text(text="Ask these questions to the bot", reply_markup=replymarkup)
        #await query.edit_message_text(text="Ask these questions to the bot", reply_markup=replymarkup)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Ask these questions to the bot", reply_markup=replymarkup)
    else:
        #calculator
        await query.edit_message_text(text=f"{message} --- {query.data}", reply_markup=InlineKeyboardMarkup(calkulatorKeyboard))

    #elif query.data == "C":
   #await query.edit_message_text(text=f"Selected language: {query.data}")


async def messageCallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    if message == "Russian🇷🇺" or message == "Русский🇷🇺":
        q1 = KeyboardButton("Что ты делаешь?")
        q2 = KeyboardButton("Как вы?")
        q3 = KeyboardButton("Где ты?")
        q4 = KeyboardButton('Как тебя зовут?')
        q5 = KeyboardButton("Сколько тебе лет?")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[q1, q2, q3], [q4, q5]], resize_keyboard=True)
        await update.message.reply_text("Задайте эти вопросы боту", reply_markup=replymarkup)
    elif message == "Меню":
        rubutton = KeyboardButton("Русский🇷🇺")
        engbutton = KeyboardButton("Английский🇺🇸")
        calculator = KeyboardButton("Калькулятор")
        replymarkup = ReplyKeyboardMarkup(keyboard= [[rubutton, engbutton], [calculator]], resize_keyboard=True)
        await update.message.reply_text(text="Выберите свой язык", reply_markup=replymarkup)
    elif message == "English🇺🇸" or message == "Английский🇺🇸":
        q1 = KeyboardButton("What are you doing?")
        q2 = KeyboardButton("How are you?")
        q3 = KeyboardButton("Where are you?")
        q4 = KeyboardButton("What is your name?")
        q5 = KeyboardButton("How old are you?")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[q1, q2, q3], [q4, q5]], resize_keyboard=True)
        await update.message.reply_text("Ask these questions to the bot", reply_markup=replymarkup)
    elif message == "Menu":
        rubutton = KeyboardButton("Russian🇷🇺")
        engbutton = KeyboardButton("English🇺🇸")
        calculator = KeyboardButton("Calculator")
        replymarkup = ReplyKeyboardMarkup(keyboard= [[rubutton, engbutton], [calculator]], resize_keyboard=True)
        await update.message.reply_text(text="Choose your language", reply_markup=replymarkup)
    elif message == "What are you doing?":
        a1 = KeyboardButton("Just sitting")
        a2 = KeyboardButton("Just lying")
        a3 = KeyboardButton("Watching TV")
        a4 = KeyboardButton("Eating")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[a1, a2, a4], [a3]], resize_keyboard=True)
        await update.message.reply_text("Nothing, what about you?", reply_markup=replymarkup)
    elif message == "How are you?":
        a1 = KeyboardButton("Bad")
        a2 = KeyboardButton("Fine")
        a3 = KeyboardButton("Good")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[a1, a2, a3]], resize_keyboard=True)
        await update.message.reply_text("I am fine, what about you?", reply_markup=replymarkup)
    elif message == "Where are you?":
        await update.message.reply_text("In your phone")               
    elif message == "Что ты делаешь?":
        a1 = KeyboardButton("Сижу")
        a2 = KeyboardButton("Лежу")
        a3 = KeyboardButton("Смотрю телевизор")
        a4 = KeyboardButton("Ем")
        replymarkup = ReplyKeyboardMarkup(keyboard= [[a1, a2, a4], [a3]], resize_keyboard=True)
        await update.message.reply_text("Ничего, а вы?", reply_markup=replymarkup)
    elif message == "What is your name?":
        await update.message.reply_text("Sharapatdin's bot")
    elif message == "How old are you?":
        await update.message.reply_text("1 month, 18 days")
    elif message == "Как вы?":
        a1 = KeyboardButton("Плохо")
        a2 = KeyboardButton("Нормально")
        a3 = KeyboardButton("Отлично")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[a1, a2, a3]], resize_keyboard=True)
        await update.message.reply_text("Хорошо, а вы", reply_markup=replymarkup)
    elif message == "Где ты?":
        await update.message.reply_text("В твоём телефоне")
    elif message == "Как тебя зовут?":
        await update.message.reply_text("Sharapatdin's bot")
    elif message == "Сколько тебе лет?":
        await update.message.reply_text("1 месяц, 18 дней")
    elif message == "Calculator" or message == "Калькулятор":
        replymarkup = InlineKeyboardMarkup(calkulatorKeyboard)
        await update.message.reply_text("Calculator", reply_markup=replymarkup)
    elif message == "Сижу":
        a1 = KeyboardButton("Плохо")
        a2 = KeyboardButton("Нормально")
        a3 = KeyboardButton("Отлично")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[a1, a2, a3]], resize_keyboard=True)
        await update.message.reply_text("Ну как сидится?", reply_markup=replymarkup) 
    elif message == "Лежу":
        a1 = KeyboardButton("Отдыхаю")
        a2 = KeyboardButton("Собираюсь спать")
        replymarkup = ReplyKeyboardMarkup([[a1, a2]], resize_keyboard=True)
        await update.message.reply_text("Просто так лежите?", reply_markup=replymarkup)
    elif message == "Смотрю телевизор":
        a1 = KeyboardButton("Спасибо")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[a1]], resize_keyboard=True)
        await update.message.reply_text("Хорошего просмотра", reply_markup=replymarkup)
    elif message == "Ем":
        a1 = KeyboardButton("Спасибо")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[a1]], resize_keyboard=True)
        await update.message.reply_text("Приятного аппетита", reply_markup=replymarkup)
    elif message == "Плохо":
        b1 = KeyboardButton("Меню")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[b1]], resize_keyboard=True)
        await update.message.reply_text("Улыбнитесь", reply_markup=replymarkup)
    elif message == "Нормально":
        b1 = KeyboardButton("Меню")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[b1]], resize_keyboard=True)
        await update.message.reply_text("Ладно", reply_markup=replymarkup)
    elif message == "Отлично":
        a1 = KeyboardButton("Спасибо")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[a1]], resize_keyboard=True)
        await update.message.reply_text("Рад слышать", reply_markup=replymarkup)
    elif message == "Спасибо":
        b1 = KeyboardButton("Меню")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[b1]], resize_keyboard=True)
        await update.message.reply_text("Не за что", reply_markup=replymarkup)
    elif message == "Отдыхаю":
        a1 = KeyboardButton("Спасибо")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[a1]], resize_keyboard=True)
        await update.message.reply_text("Хорошо отдохните", reply_markup=replymarkup)
    elif message == "Собираюсь спать":
        a1 = KeyboardButton("Спасибо")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[a1]], resize_keyboard=True)
        await update.message.reply_text("Хорошего сна", reply_markup=replymarkup)
    elif message == "Just sitting":
        a1 = KeyboardButton("Bad")
        a2 = KeyboardButton("Fine")
        a3 = KeyboardButton("Good")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[a1, a2, a3]], resize_keyboard=True)
        await update.message.reply_text("Well, how sitting?", reply_markup=replymarkup)
    elif message == "Bad":
        b1 = KeyboardButton("Menu")
        replymarkup = ReplyKeyboardMarkup([[b1]], resize_keyboard=True)
        await update.message.reply_text("Just smile", reply_markup=replymarkup)
    elif message == "Fine":
        b1 = KeyboardButton("Menu")
        replymarkup = ReplyKeyboardMarkup([[b1]], resize_keyboard=True)
        await update.message.reply_text("Ok", reply_markup=replymarkup)
    elif message == "Good":
        a1 = KeyboardButton("Thank you")
        replymarkup = ReplyKeyboardMarkup([[a1]], resize_keyboard=True)
        await update.message.reply_text("Glad to hear", reply_markup=replymarkup)
    elif message == "Thank you":
        b1 = KeyboardButton("Menu")
        replymarkup = ReplyKeyboardMarkup([[b1]], resize_keyboard=True)
        await update.message.reply_text("You are welcome", reply_markup=replymarkup)
    elif message == "Just lying":
        a1 = KeyboardButton("I am resting")
        a2 = KeyboardButton("I am going to sleep")
        replymarkup = ReplyKeyboardMarkup([[a1, a2]], resize_keyboard=True)
        await update.message.reply_text("Just lying so?", reply_markup=replymarkup)
    elif message == "I am resting":
        a1 = KeyboardButton("Thank you")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[a1]], resize_keyboard=True)
        await update.message.reply_text("Have a good rest", reply_markup=replymarkup)
    elif message == "I am going to sleep":
        a1 = KeyboardButton("Thank you")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[a1]], resize_keyboard=True)
        await update.message.reply_text("Sleep well", reply_markup=replymarkup)
    elif message == "Watching TV":
        a1 = KeyboardButton("Thank you")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[a1]], resize_keyboard=True)
        await update.message.reply_text("Have a nice watching", reply_markup=replymarkup)      
    elif message == "Eating":
        a1 = KeyboardButton("Thank you")
        replymarkup = ReplyKeyboardMarkup(keyboard=[[a1]], resize_keyboard=True)
        await update.message.reply_text("Bon appetit", reply_markup=replymarkup)
    else:
        await update.message.reply_text("wrong question")




if __name__ == '__main__':
    application = ApplicationBuilder().token('5536219218:AAHrE4bI1fxDlD88TxWNGv6_oqb-gl5DFRw').build()
    
    start_handler = CommandHandler('start', startCallback)
    begin_handler = CommandHandler('begin', startCallback)
    message_handler = MessageHandler(filters.TEXT, messageCallback)
    callback_query_handler = CallbackQueryHandler(inlineButtonCallback)

    application.add_handler(start_handler)
    application.add_handler(begin_handler)
    application.add_handler(message_handler)
    application.add_handler(callback_query_handler)
    
    application.run_polling()