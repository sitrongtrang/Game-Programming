from data import constant
from BaseItem import BaseItem

class HealItem(BaseItem):
    def __init__(self, x, y, width, height):
        super.__init__(x, y, width, height)
        self.heal_amount = constant.heal_amount

    def takeEffect(self, character):
        character.setHealth(character.getHealth() + self.heal_amount)