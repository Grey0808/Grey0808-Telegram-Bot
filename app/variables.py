import telebot


# bot
with open("files/key.txt", "r") as file:
    key = file.read()

bot = telebot.TeleBot(key)


# keyboards
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока', 'Время', 'Баланс')
keyboard1.row('Казино', 'Минное поле', 'Мини рулетка')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Правила', 'Баланс')
keyboard2.row('Назад')


# parity
chet = ['чёт', 'чет', 'чётное', 'четное', 'ч']
nechet = ['нечёт', 'нечет', 'нечётное', 'нечетное', 'н']


# admins
admins = (454049569, )
