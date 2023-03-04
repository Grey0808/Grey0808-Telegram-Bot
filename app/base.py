import pickle
import app.player as player


def readbase():
    with open('files/base.txt', 'rb+') as file:
        return pickle.load(file)


def savebase(users):
    with open('files/base.txt', 'wb') as file:
        pickle.dump(users, file)
