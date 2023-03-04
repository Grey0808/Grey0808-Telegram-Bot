import app.variables as var
import app.base as base

bot = var.bot


class Player:
    def __init__(self, _id: int, _money=500, _gamemode=1, _admin=0):
        self.id = _id
        self.__money = _money
        self.__gamemode = _gamemode
        self.curr_keyboard = var.keyboard1
        self.admin = _admin

    def send(self, string):
        bot.send_message(self.id, string, reply_markup=self.curr_keyboard)

    def tuple(self):
        return self.id, self.__money, self.__gamemode, self.admin

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        base.update(self.id, "money", money)
        self.__money = money

    @property
    def gamemode(self):
        return self.__gamemode

    @gamemode.setter
    def gamemode(self, gamemode):
        base.update(self.id, "gamemode", gamemode)
        if gamemode == 1:
            self.curr_keyboard = var.keyboard1
        elif gamemode in (2, 3, 4):
            self.curr_keyboard = var.keyboard2
        self.__gamemode = gamemode
