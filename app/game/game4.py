import app.rand as rand
import app.variables as var
import app.base as base

# keyboard
keyboard1 = var.keyboard1
keyboard2 = var.keyboard2

# parity
chet = var.chet
nechet = var.nechet


# мини рулетка
def game4(message, mess, curruser):
    if mess == 'правила':
        curruser.send(
            'Всего есть 38 чисел, от 1 до 36 и два 0, выбирается случайное. '
            'Ты можешь ставить будет это число чётным или нечётным и выиграть с плюсом ×2, если это будет 0, то ×5. '
            'Но если ты проиграешь ставка пропадает. Удачи!')
        curruser.send(
            'В качестве чётного или нечётного можно вводить:'
            '\nнечёт/нечет/нечётное/нечетное/н '
            '\nчёт/чет/чётноe/четное/ч')
        curruser.send('Введите ставку и чётное/нечётное:')

    elif mess == 'назад':
        curruser.gamemode = 1
        curruser.send('Ждём вас снова')

    elif mess == 'баланс':
        curruser.send('В твоём кошельке ' + str(curruser.money) + '₽')

    elif len(mess.split(" ")) == 2:
        mess = mess.split(" ")
        if mess[0].isdigit() and mess[1] in (chet + nechet):
            mess[0] = int(mess[0])
            if curruser.money >= 10:
                if 10 <= mess[0] <= curruser.money:
                    logsname = message.chat.first_name + " " + message.chat.username
                    logsmoney = curruser.money

                    number = rand.randint(0, 37)
                    if number == 37:
                        number = 0

                    ischet = number % 2 == 0
                    a = True if mess[1].lower() in chet else False
                    b = True if mess[1].lower() in nechet else False

                    win = 0
                    if number == 0:
                        win = 2
                    elif a and ischet:
                        win = 1
                    elif b and not ischet:
                        win = 1

                    curruser.send('На барабане число ' + str(number))
                    if win == 0:
                        curruser.money -= mess[0]
                        curruser.send('Ты проиграл ' + str(mess[0]) + '₽')
                    elif win == 1:
                        curruser.money += mess[0]
                        curruser.send('Прямо в точку! Ты забрал ' + str(mess[0]) + '₽')
                    elif win == 2:
                        curruser.money -= mess[0]
                        curruser.send('Выпал 0, ты проиграл ' + str(mess[0]) + '₽')

                    print(logsname, logsmoney, curruser.money - logsmoney, curruser.money)

                elif int(mess[0]) < 10:
                    curruser.send('Меньше 10 нельзя')
                elif int(mess[0]) > curruser.money:
                    curruser.send('Куда так много')
            elif curruser.money < 10:
                curruser.send('У тебя не хватает денег')
