import pygame
from data import constant

class BaseItem:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.appear_duration = constant.ITEM_APPEAR_DUR
        self.effect_duration = constant.ITEM_EFFECT_DUR
        self.picked_up = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 100), self.rect)
    
    def takeEffect(self, character):
        raise NotImplementedError
    
    def update(self, screen, deltaTime):
        if not self.picked_up:
            self.draw(screen)
            self.appear_duration -= deltaTime
        else:
            self.effect_duration -= deltaTime

    def pickedUp(self, character):
        self.picked_up = True
        self.takeEffect(character)

