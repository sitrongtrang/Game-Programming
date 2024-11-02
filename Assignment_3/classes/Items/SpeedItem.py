from data import constant
from .BaseItem import BaseItem

class SpeedItem(BaseItem):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.speed_increase_coeff = constant.SPEED_INCREASE_COEFF

    def takeEffect(self, character):
        self.char_speed_before = character.speed
        self.char_picked_up = character
        character.setSpeed(character.speed * self.speed_increase_coeff)

    def update(self, screen, deltaTime, camera_x=0):
        super().update(screen, deltaTime, camera_x)
        if self.effect_duration <= 0:
            self.char_picked_up.speed = self.char_speed_before 
