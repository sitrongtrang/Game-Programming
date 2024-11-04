import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, all_sprites, x, y, width, height):
        super().__init__()

        all_sprites.add(self)
        self.all_sprites = all_sprites

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 0))  # Yellow color for placeholder

        # Rect attributes
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen, camera_x=0):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y, self.rect.width, self.rect.height))
