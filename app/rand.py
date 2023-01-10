import secrets

rnd = secrets.SystemRandom()
print("new rand")


def random(procent):
    if rnd.random() * 100 < procent:
        return True
    else:
        return False


def randint(a, b):
    return rnd.randint(a, b)
