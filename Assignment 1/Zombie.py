import pygame
from random import randint

stunned_image = pygame.image.load('sprites/stunned.png')

class Zombie:
    def __init__(self, x, y, width, height, sprite_image) -> None:
        self.appear_time = pygame.time.get_ticks()
        self.stay_time = randint(3000, 5000)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.sprite = pygame.transform.scale(sprite_image, (self.width, self.height))
        self.stunned_sprite = pygame.transform.scale(stunned_image, (self.width, self.height))  # Scale stunned image
        self.stunned_start_time = None

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
        if self.stunned_start_time is not None:
            screen.blit(self.stunned_sprite, (self.x, self.y-self.width//2))

    def stun(self):
        self.stunned_start_time = pygame.time.get_ticks()

    def is_stunned_for_duration(self):
        # Check if 1 second has passed since the zombie was stunned
        return self.stunned_start_time is not None and pygame.time.get_ticks() - self.stunned_start_time >= 1000


    def is_smashed(self, pos):
        if self.stunned_start_time is None:
            return pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(pos)
        return False