import app.rand as rand
import app.variables as var
import app.messages as messages

# keyboard
keyboard1 = var.keyboard1
keyboard2 = var.keyboard2


# минное поле
def game3(message, mess, curruser):

    if mess == 'правила':
        curruser.send(
            'На поле, размером 3×3 расположено 6 мин. Шансы выиграть 4 к 9. В случае выигрыша вы получите 200%, '
            'в случае проигрыша ставка сгорает')
        curruser.send('Введите сначала ставку и через пробел номер клетки от 1 до 9:')

    elif mess == 'назад':
        curruser.gamemode = 1
        curruser.send('Приходите к нам почаще')

    elif mess == 'баланс':
        curruser.send('Сейчас ты богат на ' + str(curruser.money) + '₽')

    elif len(mess.split(" ")) == 2:
        mess = mess.split(" ")
        if mess[0].isdigit() and mess[1].isdigit():
            mess = list(map(int, mess))
            if curruser.money >= 10 and 1 <= mess[1] <= 9:
                if 10 <= mess[0] <= int(curruser.money):
                    logsname = message.chat.first_name + " " + message.chat.username
                    logsmoney = curruser.money

                    ind = set()
                    while len(ind) != 4:
                        ind.add(rand.randint(1, 9))
                    ind = sorted(list(ind))

                    keyboardfield = messages.startfield(curruser, ind)
                    curruser.curr_keyboard = keyboardfield
                    curruser.send('Поле:')

                    curruser.curr_keyboard = keyboard2
                    elem = ""
                    for i in ind:
                        elem += str(i) + " "
                    curruser.send('Выпали клетки ' + elem)

                    if ind.count(mess[1]) != 0:
                        curruser.money += mess[0]
                        curruser.send('Ура, ты не взорвался и забрал +' + str(mess[0]) + '₽')
                    else:
                        curruser.money -= mess[0]
                        curruser.send('Ты взорвался')
                    print(logsname, logsmoney, curruser.money - logsmoney, curruser.money)
                elif mess[0] < 10:
                    curruser.send('Меньше 10 нельзя')
                elif mess[0] > curruser.money:
                    curruser.send('Куда так много')
            elif curruser.money < 10:
                curruser.send('У тебя нехватает денег')
            elif mess[1] > 9 or mess[1] < 1:
                curruser.send('Такой клетки нет')
