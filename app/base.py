import pickle


def readbase(values):
    with open('files/base.txt', 'rb+') as file:
        try:
            users = pickle.load(file)
        except BaseException as Error:
            print("err", Error)
            pickle.dump([], file)
    values["users"] = users


def savebase(values):
    with open('files/base.txt', 'wb') as file:
        pickle.dump(values["users"], file)
