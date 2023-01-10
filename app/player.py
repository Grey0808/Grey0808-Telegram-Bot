import app.variables as var

bot = var.bot


class Player(object):
    def __init__(self, _id):
        self.id = _id

        self.money = 500
        self.gamemode = 0
        self.curr_keyboard = var.keyboard1

    def send(self, string):
        bot.send_message(self.id, string, reply_markup=self.curr_keyboard)
