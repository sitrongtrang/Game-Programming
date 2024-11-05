import pygame
from .BaseItem import BaseItem
from data import constant
class JumpItem(BaseItem):
    JUMP_COEFF  = 2
    def __init__(self, all_sprites, x, y, width=constant.TILE_SIZE, height=constant.TILE_SIZE):
        super().__init__(all_sprites, x, y, width, height)
        self.load_img("assets\\sprites\\items\\jump.png")

    def takeEffect(self, character):
        self.char_jump_before = character.jump
        self.char_picked_up = character
        character.setJump(character.jump * JumpItem.JUMP_COEFF)

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
                self.char_picked_up.jump = self.char_jump_before
                self.kill() 