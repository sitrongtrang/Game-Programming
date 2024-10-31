from data import constant
from BaseItem import BaseItem

class DmgItem(BaseItem):
    def __init__(self, x, y, width, height):
        super.__init__(x, y, width, height)
        self.dmg_increase_coeff = constant.dmg_increase_coeff

    def takeEffect(self, character):
        character.setDmg(character.getDmg() * self.dmg_increase_coeff)
