from data import constant
from .BaseItem import BaseItem

class DmgItem(BaseItem):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dmg_increase_coeff = constant.DMG_INCREASE_COEFF

    def takeEffect(self, character):
        character.setDmg(character.dmg * self.dmg_increase_coeff)
