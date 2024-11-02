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
        self.previous_ticks = pygame.time.get_ticks()

    def draw(self, screen, camera_x=0):
        pygame.draw.rect(screen, (0, 255, 0), (self.rect.x - camera_x, self.rect.y, self.width, self.height))
    
    def takeEffect(self, character):
        raise NotImplementedError
    
    def update(self, screen, items, camera_x=0):
        deltaTime = pygame.time.get_ticks() - self.previous_ticks
        self.previous_ticks = pygame.time.get_ticks()
        if not self.picked_up:
            self.draw(screen, camera_x)
            self.appear_duration -= deltaTime
            if self.appear_duration <= 0:
                items.remove(self)
        else:
            self.effect_duration -= deltaTime
            if self.effect_duration <= 0:
                items.remove(self)

    def pickedUp(self, character):
        self.rect = None
        self.picked_up = True
        self.takeEffect(character)

