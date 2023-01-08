from datetime import datetime
import random

import app.variables as var
import app.base as base

import app.game.game0 as game0
import app.game.game1 as game1
import app.game.game2 as game2
import app.game.game3 as game3

# keyboard
keyboard1 = var.keyboard1
keyboard2 = var.keyboard2

# admins
admins = var.admins


def send_text(values, message):
    users = values["users"]
    # bot = values["bot"]

    def savebase():
        base.savebase(values)

    mess = message.text.lower()
    # messorig = message.text

    for i in range(len(users)):
        if users[i].id == message.chat.id:
            curruser = users[i]
            break

    # if curruser.id in admins:
        # pass
        # adm.admin(values, message, mess, curruser)

    if curruser.gamemode == 0:
        game0.game0(savebase, message, mess, curruser)

    elif curruser.gamemode == 1:
        game1.game1(savebase, message, mess, curruser)

    elif curruser.gamemode == 2:
        game2.game2(savebase, message, mess, curruser)

    elif curruser.gamemode == 3:
        game3.game3(savebase, message, mess, curruser)

    # if curruser.id != 454049569:
    #     bot.send_message(454049569, message.chat.first_name + ' написал: ' + str(message.text))
