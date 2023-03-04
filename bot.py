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


# call.data == "not"
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    data = [func(inf) for inf, func in zip(call.data.split("_"), (int, int, int, str))]
    data = dict(zip(["id", "gamemode", "admin_menu", "text"], data))
    data["call"] = call.id
    if not data["admin_menu"]:
        mess.callback_worker(bot, data)


@bot.message_handler(content_types=['text'])
def send_text(message):
    game.send_text(users, message)


bot.polling()
