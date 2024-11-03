import pygame
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

    def update(self):
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
