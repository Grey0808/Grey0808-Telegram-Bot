from datetime import datetime
import random

import app.variables as var
import app.base as base

import app.game.game0 as game0
import app.game.game1 as game1
import app.game.game2 as game2
import app.game.game3 as game3

import app.messages as mess

# keyboard
keyboard1 = var.keyboard1
keyboard2 = var.keyboard2

# admins
admins = var.admins


def send_text(users, message):
    def savebase():
        base.savebase(users)

    msg = message.text.lower()

    if not users.get(message.chat.id):
        mess.start_message(users, message, False)
    curruser = users[message.chat.id]

    if curruser.admin_menu:
        pass

    elif curruser.gamemode == 0:
        game0.game0(savebase, message, msg, curruser)

    elif curruser.gamemode == 1:
        game1.game1(savebase, message, msg, curruser)

    elif curruser.gamemode == 2:
        game2.game2(savebase, message, msg, curruser)

    elif curruser.gamemode == 3:
        game3.game3(savebase, message, msg, curruser)
