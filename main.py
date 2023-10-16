import telebot

bot = telebot.TeleBot("6135119530:AAGSqjhlYh9hnFdPE5LMyDAq8jm7PrOCDQM")

@bot.message_handler (commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Hello👋 Just testing stuff")
    
bot.polling()    