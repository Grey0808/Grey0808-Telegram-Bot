import telebot
import app.messages as mess
import app.variables as var
import app.games as game
import app.base as base

# bot
bot = var.bot
users = base.readbase()
base.savebase(users)
print(len(users))


@bot.message_handler(commands=['start'])
def start_message(message):
    mess.start_message(users, message)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    mess.callback_worker(bot, call)


@bot.message_handler(content_types=['text'])
def send_text(message):
    game.send_text(users, message)


bot.polling()
