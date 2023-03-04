import configparser

import telebot
import mysql.connector

# bot
with open("files/key.txt", "r") as file:
    key = file.read()

bot = telebot.TeleBot(key)


# keyboards
keyboards = {}

keyboard0 = telebot.types.ReplyKeyboardMarkup(True)
keyboards[0] = keyboard0

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Время', 'Баланс')
keyboard1.row('Казино', 'Минное поле', 'Мини рулетка')
keyboards[1] = keyboard1

keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Правила', 'Баланс')
keyboard2.row('Назад')
keyboards[2] = keyboard1


# parity
chet = ['чёт', 'чет', 'чётное', 'четное', 'ч']
nechet = ['нечёт', 'нечет', 'нечётное', 'нечетное', 'н']


# admins
admins = (454049569, )


# database
config = configparser.ConfigParser()
with open("files/connector.ini") as file:
    config.read_file(file)
connector = config.defaults()
conn = mysql.connector.connect(**connector)
cur = conn.cursor()
