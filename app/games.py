import app.base as base

import app.game.game1 as game1
import app.game.game2 as game2
import app.game.game3 as game3
import app.game.game4 as game4

import app.messages as mess


def send_text(users, message):
    msg = message.text.lower()

    if not users.get(message.chat.id):
        mess.start_message(users, message, False)
    curruser = users[message.chat.id]

    if curruser.admin:
        ...

    elif curruser.gamemode == 1:
        game1.game1(message, msg, curruser)

    elif curruser.gamemode == 2:
        game2.game2(message, msg, curruser)

    elif curruser.gamemode == 3:
        game3.game3(message, msg, curruser)

    elif curruser.gamemode == 4:
        game4.game4(message, msg, curruser)
