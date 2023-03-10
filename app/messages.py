import telebot
from app.player import Player
import app.base as base


def start_message(users, message):
    information = [message.chat.id, message.chat.username, message.chat.first_name, message.chat.last_name]
    print(*information)

    if not users.get(message.chat.id):
        users[message.chat.id] = Player(message.chat.id)
        base.savebase(users)

    curruser = users[message.chat.id]
    curruser.send('Привет, ты написал мне /start')


def callback_worker(bot, call):
    bot.answer_callback_query(call.id, "Не сюда нажимай")


def startfield(ind):
    cell = ['◼' for _ in range(9)]
    for i in ind:
        cell[i - 1] = '◻'

    def button(num):
        return telebot.types.InlineKeyboardButton(cell[num], callback_data='not')

    keyboardfield = telebot.types.InlineKeyboardMarkup()
    for j in (0, 3, 6):
        keyboardfield.row(*[button(i) for i in range(j, j + 3)])
    return keyboardfield
