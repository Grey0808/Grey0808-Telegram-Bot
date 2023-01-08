import telebot
from app.player import Player
import app.base as base


def start_message(values: dict, message) -> None:
    users = values["users"]
    bot = values["bot"]

    information = [message.chat.id, message.chat.username, message.chat.first_name, message.chat.last_name]
    print(*information)

    new = True
    for i in range(len(users)):
        if users[i].id == message.chat.id:
            print('old')
            new = False
            break
    if new:
        values["users"] += [Player(message.chat.id)]
        base.savebase(values)
        print('new')

    for i in range(len(users)):
        if users[i].id == message.chat.id:
            curruser = users[i]
            break
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=curruser.curr_keyboard)


def callback_worker(values: dict, call) -> None:
    bot = values["bot"]
    bot.send_message(call.message.chat.id, "Не сюда нажимай")
    bot.answer_callback_query(call.id)


def startfield(ind):
    cell = ['◼' for _ in range(9)]
    for i in ind:
        cell[i - 1] = '◻'
    keyboardfield = telebot.types.InlineKeyboardMarkup()
    keyboardfield .row(
            telebot.types.InlineKeyboardButton(cell[0], callback_data='get'),
            telebot.types.InlineKeyboardButton(cell[1], callback_data='get'),
            telebot.types.InlineKeyboardButton(cell[2], callback_data='get')
        )
    keyboardfield .row(
            telebot.types.InlineKeyboardButton(cell[3], callback_data='get'),
            telebot.types.InlineKeyboardButton(cell[4], callback_data='get'),
            telebot.types.InlineKeyboardButton(cell[5], callback_data='get'),
        )
    keyboardfield .row(
            telebot.types.InlineKeyboardButton(cell[6], callback_data='get'),
            telebot.types.InlineKeyboardButton(cell[7], callback_data='get'),
            telebot.types.InlineKeyboardButton(cell[8], callback_data='get'),
        )
    return keyboardfield
