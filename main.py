import telebot
import token_for_bot

bot = telebot.TeleBot(token_for_bot.token)

def open_file(path):
    str = ''
    file = open(path, "r")

    for line in file:
        str += line

    return str

@bot.message_handler(commands=['пн'])
def send_welcome(message):
	bot.reply_to(message, open_file("msg/pn.txt"))

@bot.message_handler(commands=['вт'])
def send_welcome(message):
	bot.reply_to(message, open_file("msg/wt.txt"))

@bot.message_handler(commands=['ср'])
def send_welcome(message):
	bot.reply_to(message, open_file("msg/sr.txt"))

@bot.message_handler(commands=['чт'])
def send_welcome(message):
	bot.reply_to(message, open_file("msg/cht.txt"))

@bot.message_handler(commands=['пт'])
def send_welcome(message):
	bot.reply_to(message, open_file("msg/pt.txt"))

@bot.message_handler(commands=['start' , 'help'])
def send_welcome(message):
	bot.reply_to(message, open_file("msg/help.txt"))


bot.polling()
