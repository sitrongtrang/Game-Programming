import pygame


class BaseItem:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (0, 255, 100), rect)
    
    def takeEffect(self, character):
        raise NotImplementedError
