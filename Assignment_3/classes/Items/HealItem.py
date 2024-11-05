from data import constant
from .BaseItem import BaseItem

class HealItem(BaseItem):
    def __init__(self, all_sprites, x, y, width=constant.TILE_SIZE, height=constant.TILE_SIZE):
        super().__init__(all_sprites, x, y, width, height)
        self.heal_amount = constant.HEAL_AMOUNT
        self.load_img("assets\\sprites\\items\\heal.png")

    def takeEffect(self, character):
        character.setHP(character.hp + self.heal_amount)
