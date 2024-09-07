import pygame
from random import randint

class Zombie:
    def __init__(self, x, y, width, height, sprite_image) -> None:
        self.appear_time = pygame.time.get_ticks()
        self.stay_time = randint(3000, 5000)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.sprite = pygame.transform.scale(sprite_image, (self.width, self.height))

    def draw(self, screen):
        # pygame.draw.rect(screen, green, (self.x, self.y, self.width, self.height))
        screen.blit(self.sprite, (self.x, self.y))

    def is_smashed(self, pos):
        return pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(pos)