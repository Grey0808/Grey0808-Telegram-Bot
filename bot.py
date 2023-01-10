import telebot
import app.messages as mess
import app.variables as var
import app.games as game
import app.base as base

# bot
bot = var.bot
values = {"bot": bot, "users": []}
base.readbase(values)
base.savebase(values)
print(len(values["users"]))


@bot.message_handler(commands=['start'])
def start_message(message):
    global values
    mess.start_message(values, message)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global values
    mess.callback_worker(values, call)


@bot.message_handler(content_types=['text'])
def send_text(message):
    global values
    game.send_text(values, message)


bot.polling()
