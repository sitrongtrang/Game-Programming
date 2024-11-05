import pygame
from classes.Items.AllItem import *

class Barrel(pygame.sprite.Sprite):
    from random import choice as _random
    RATE = [True, True * 2]
    def __init__(self, all_sprites, x, y, game_manager):
        super().__init__()
        self.all_sprites = all_sprites
        all_sprites.add(self)
        self.x = x
        self.y = y
        self.image = pygame.Surface((32, 32)) # Set size of barrel
        # self.image.fill((100, 255, 100))  # Green color for barrels
        self.load_img("assets\\sprites\\barrel.png")
    
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.game_manager = game_manager
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
        item = self.item(self.all_sprites, self.rect.x, self.rect.y, 32, 32)
        self.game_manager.items.add(item)
        return item

    def void(self):
        return
    
    def draw(self, screen, camera_x=0):
        if self.image:
            screen.blit(self.image, (self.rect.x - camera_x, self.rect.y, self.rect.width, self.rect.height))

    def load_img(self, filePath):
        try:
            # Load the bullet image
            self.image = pygame.image.load(filePath).convert_alpha()
            # Scale the image to fit the dimensions of self.img
            self.image = pygame.transform.scale(self.image, self.image.get_size())
        except pygame.error:
            print("Unable to load bullet image.")
            raise SystemExit