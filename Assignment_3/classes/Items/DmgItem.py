from data import constant
from .BaseItem import BaseItem

class DmgItem(BaseItem):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dmg_increase_coeff = constant.DMG_INCREASE_COEFF

    def takeEffect(self, character):
        self.char_dmg_before = character.dmg
        self.char_picked_up = character
        character.setDmg(character.dmg * self.dmg_increase_coeff)

    def update(self, screen, deltaTime):
        super().update(screen, deltaTime)
        if self.effect_duration <= 0:
            self.char_picked_up.dmg = self.char_dmg_before 