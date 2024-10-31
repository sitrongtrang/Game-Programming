import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,all_sprites, x, y, direction="right"):
        super().__init__()
        self.all_sprites = all_sprites
        all_sprites.add(self)
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 0, 0))  # Red color for bullets
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 8 if direction == "right" else -8  # Set speed based on direction

    def update(self):
        self.rect.x += self.speed  # Move bullet in the set direction
        # Remove bullet if it goes off screen
        if self.rect.x > 800 or self.rect.x < 0:
            self.kill()
