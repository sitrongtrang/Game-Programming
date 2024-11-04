import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, all_sprites, x, y, width, height):
        super().__init__()

        all_sprites.add(self)
        self.all_sprites = all_sprites

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.image = pygame.Surface((width, height))
        self.image.fill((150, 75, 0))  # Blue color for placeholder

        # Rect attributes
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, camera_x=0):
        pass

