import telebot
import token_for_bot

bot = telebot.TeleBot(token_for_bot.token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


bot.polling()
