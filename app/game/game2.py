import app.rand as rand
import app.variables as var

# keyboard
keyboard1 = var.keyboard1
keyboard2 = var.keyboard2


# казино
def game2(message, mess, curruser):

    if mess == 'правила':
        curruser.send('Вероятность победы 0,33. '
                      'В случае выигрыша вы получите 300%, в случае проигрыша ставка исчезает')
        curruser.send('Введите ставку')

    elif mess == 'назад':
        curruser.gamemode = 1
        curruser.send('Ждём вас снова')

    elif mess == 'баланс':
        curruser.send('Сейчас на счету у тебя ' + str(curruser.money) + '₽')

    elif mess.isdigit():
        mess = int(mess)
        if curruser.money >= 10:
            if 10 <= mess <= curruser.money:
                logsname = message.chat.first_name + " " + message.chat.username
                logsmoney = curruser.money
                if rand.random(33):
                    curruser.money += mess * 2
                    curruser.send('Ты победил и заработал +' + str(mess * 2) + '₽')
                else:
                    curruser.money -= mess
                    curruser.send('Не повезло, ты проиграл')
                print(logsname, logsmoney, curruser.money - logsmoney, curruser.money)
            elif mess < 10:
                curruser.send('Минимальная ставка - 10')
            elif mess > curruser.money:
                curruser.send('У вас столько нет')
        elif curruser.money < 10:
            curruser.send('Ты банкрот, у тебя ' + str(curruser.money) + '₽')
