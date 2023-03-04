from datetime import datetime
import app.variables as var

# keyboard
keyboard1 = var.keyboard1
keyboard2 = var.keyboard2


def game1(message, mess, curruser):

    if mess == 'привет':
        curruser.send('Привет, ' + message.chat.first_name)
    elif mess == 'время':
        time = datetime.fromtimestamp(message.date, tz=None).strftime('%H:%M:%S %d.%m.%Y')
        curruser.send('На ваших часах сейчас примерно:\n' + time)
    elif mess == 'баланс':
        curruser.send('На твоём счету ' + str(curruser.money) + '₽')

    elif mess == 'казино':
        curruser.gamemode = 2
        curruser.send('Добро пожаловать в казино')
    elif mess == 'минное поле':
        curruser.gamemode = 3
        curruser.send('Добро пожаловать на минное поле')
    elif mess == 'мини рулетка':
        curruser.gamemode = 4
        curruser.send('Добро пожаловать в мини рулетку')
