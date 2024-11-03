from data import constant
from .BaseItem import BaseItem

class BulletItem(BaseItem):
    def __init__(self, all_sprites, x, y, width, height):
        super().__init__(all_sprites, x, y, width, height)
        self.bullet_resupply = constant.BULLET_RESUPPLY

    def takeEffect(self, character):
        character.setBullet(character.bullet + self.bullet_resupply)
