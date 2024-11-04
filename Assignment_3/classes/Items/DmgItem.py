import pygame
from data import constant
from .BaseItem import BaseItem

class DmgItem(BaseItem):
    def __init__(self, all_sprites, x, y, width, height):
        super().__init__(all_sprites, x, y, width, height)
        self.dmg_increase_coeff = constant.DMG_INCREASE_COEFF

    def takeEffect(self, character):
        self.char_dmg_before = character.dmg
        self.char_picked_up = character
        character.setDmg(character.dmg * self.dmg_increase_coeff)

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
                self.char_picked_up.dmg = self.char_dmg_before 
                self.kill()