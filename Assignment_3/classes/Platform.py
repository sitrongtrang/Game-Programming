import pygame

class Platform:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen, camera_x=0):
        pygame.draw.rect(screen, (150, 75, 0), (self.rect.x - camera_x, self.rect.y, self.width, self.height))

    def update(self, screen, camera_x=0):
        self.draw(screen, camera_x)
