import os
import pickle

if not os.path.isdir("files"):
    os.mkdir("files")

os.chdir("files")
if not os.path.exists('key.txt') or os.stat("key.txt").st_size == 0:
    with open("key.txt", "w") as file:
        key = input("Введите ключ бота: ")
        file.write(key)

# need refactor
with open("connector.ini", "w") as file:
    text = '''[DEFAULT]
host=127.0.0.1
port=3306
user=root
password=1212
database=test'''
    file.write(text)
