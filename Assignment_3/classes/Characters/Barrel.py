import pygame
from classes.Items.AllItem import *

class Barrel(pygame.sprite.Sprite):
    from random import choice as _random
    RATE = [True, False * 2]
    def __init__(self, all_sprites, x, y):
        super().__init__()
        self.all_sprites = all_sprites
        all_sprites.add(self)
        self.x = x
        self.y = y
        self.image = pygame.Surface((32, 32)) # Set size of barrel
        self.image.fill((100, 255, 100))  # Green color for barrels
    
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # it can contain a random item

        self.item = Barrel.lucky_barrel()
        self.on_destroy = self.drop_item if self.item else self.void

    @staticmethod
    def lucky_barrel():
        if Barrel._random(Barrel.RATE):
            return random_item()
        return None
    
    def destroy(self):
        self.on_destroy()
        self.kill()

    def drop_item(self):
        return self.item(self.all_sprites, self.rect.x, self.rect.y)

    def void(self):
        return