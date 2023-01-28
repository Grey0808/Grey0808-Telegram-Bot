from datetime import datetime
import app.variables as var

# keyboard
keyboard1 = var.keyboard1
keyboard2 = var.keyboard2


def game0(savebase, message, mess, curruser):

    if mess == 'привет':
        curruser.send('Привет, ' + message.chat.first_name)
    elif mess == 'время':
        time = datetime.fromtimestamp(message.date, tz=None).strftime('%H:%M:%S %d.%m.%Y')
        curruser.send('На ваших часах сейчас примерно:\n' + time)
    elif mess == 'баланс':
        curruser.send('На твоём счету ' + str(curruser.money) + '₽')

    elif mess == 'казино':
        curruser.curr_keyboard = keyboard2
        curruser.send('Добро пожаловать в казино')
        curruser.gamemode = 1
        savebase()
    elif mess == 'минное поле':
        curruser.curr_keyboard = keyboard2
        curruser.send('Добро пожаловать на минное поле')
        curruser.gamemode = 2
        savebase()
    elif mess == 'мини рулетка':
        curruser.curr_keyboard = keyboard2
        curruser.send('Добро пожаловать в мини рулетку')
        curruser.gamemode = 3
        savebase()
