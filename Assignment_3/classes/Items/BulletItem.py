from data import constant
from .BaseItem import BaseItem

class BulletItem(BaseItem):
    def __init__(self, all_sprites, x, y, width=constant.TILE_SIZE, height=constant.TILE_SIZE):
        super().__init__(all_sprites, x, y, width, height)
        self.bullet_resupply = constant.BULLET_RESUPPLY
        self.load_img("assets\\sprites\\items\\ammo.png")

    def takeEffect(self, character):
        character.setBullet(character.bullet + self.bullet_resupply)
