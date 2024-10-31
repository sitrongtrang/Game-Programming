from data import constant
from BaseItem import BaseItem

class SpeedItem(BaseItem):
    def __init__(self, x, y, width, height):
        super.__init__(x, y, width, height)
        self.speed_increase_coeff = constant.speed_increase_coeff

    def takeEffect(self, character):
        character.setSpeed(character.getSpeed() * self.speed_increase_coeff)
