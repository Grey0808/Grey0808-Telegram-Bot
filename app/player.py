import app.variables as var

# keyboard
keyboard1 = var.keyboard1
keyboard2 = var.keyboard2
bot = var.bot


class Player(object):
    def __init__(self, id, money=500, gamemode=0, curr_keyboard=0):
        self.id = id
        self.money = money
        self.gamemode = gamemode
        if curr_keyboard == 0:
            self.curr_keyboard = keyboard1
        elif curr_keyboard == 1:
            self.curr_keyboard = keyboard2

    def send(self, string: str):
        bot.send_message(self.id, string, reply_markup=self.curr_keyboard)

        if self.money < 10:
            self.money = 500
            bot.send_message(self.id, "Боги откатили твой баланс до 500₽", reply_markup=self.curr_keyboard)

    def getinfo(self):
        return str(self.id) + " " + str(self.money)
