import os
import pickle

if not os.path.isdir("files"):
    os.mkdir("files")

os.chdir("files")
with open("key.txt", "w") as file:
    key = input("Введите ключ бота: ")
    file.write(key)
with open("base.txt", "wb") as file:
    pickle.dump({}, file)
