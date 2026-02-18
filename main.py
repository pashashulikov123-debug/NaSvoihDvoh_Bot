import telebot

TOKEN = "8527162244:AAGqC22orGnJGq9TJpEnBXyht_FmbaLaUt4"
ADMIN_ID = 777545466

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def forward(message):
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)

print("Bot started...")
bot.polling()
