import pygame
from data import constant
from .BaseItem import BaseItem

class SpeedItem(BaseItem):
    def __init__(self, all_sprites, x, y, width=constant.TILE_SIZE, height=constant.TILE_SIZE):
        super().__init__(all_sprites, x, y, width, height)
        self.speed_increase_coeff = constant.SPEED_INCREASE_COEFF
        self.load_img("assets\\sprites\\items\\speed.png",  width, height)

    def takeEffect(self, character):
        self.char_speed_before = character.speed
        self.char_picked_up = character
        character.setSpeed(character.speed * self.speed_increase_coeff)

    def update(self, camera_x=0):
        deltaTime = pygame.time.get_ticks() - self.previous_ticks
        self.previous_ticks = pygame.time.get_ticks()
        if not self.picked_up:
            self.appear_duration -= deltaTime
            if self.appear_duration <= 0:
                self.kill()
        else:
            self.effect_duration -= deltaTime
            if self.effect_duration <= 0:
                self.char_picked_up.speed = self.char_speed_before 
                self.kill()
