import pygame
import math
from data import constant

class Bullet(pygame.sprite.Sprite):
    def __init__(self, all_sprites, x, y, direction="right"):
        super().__init__()
        self.all_sprites = all_sprites
        all_sprites.add(self)
        self.image = pygame.Surface((10, 5))
    #    self.image.fill((255, 0, 0))  # Red color for bullets
        self.rect = self.image.get_rect(center=(x, y))
        self.origin_x = x
        self.origin_y = y
        self.speed = constant.BOSS_SPEED if direction == "right" else -constant.BOSS_SPEED  # Set speed based on direction

    def load_img(self, filePath):
        try:
            # Load the bullet image
            self.image = pygame.image.load(filePath).convert_alpha()
        except pygame.error:
            print("Unable to load bullet image.")
            raise SystemExit
    def draw(self, screen, camera_x=0):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y, self.rect.width, self.rect.height))

    def update(self, camera_x=0):
        if (self.rect.x - self.origin_x) ** 2 + (self.rect.y - self.origin_y) ** 2 > constant.BULLET_RANGE ** 2:
            self.kill()


class Bullet_Enemy(Bullet):
    def __init__(self,all_sprites, x, y, direction="right"):
        super().__init__(all_sprites, x, y, direction)
        self.load_img("assets\\sprites\\enemy_bullet.png")

    def update(self, camera_x=0):
        self.rect.x += self.speed
        super().update(camera_x)


class Bullet_Player(Bullet):
    def __init__(self, all_sprites, x, y, angle, direction="right"):
        super().__init__(all_sprites, x, y)
        self.load_img("assets\\sprites\\bullet.png")
        # Adjust angle based on direction
        # if direction == "left":
        #     angle += math.pi  # Flip angle for leftward shooting

        # Calculate velocity based on the angle
          # Adjust as needed
        self.velocity_x = constant.BULLET_SPEED * math.cos(angle)
        self.velocity_y = constant.BULLET_SPEED * math.sin(angle)

    def update(self, camera_x=0):
        # Move the bullet in the direction of the angle
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        # Remove the bullet if it goes off-screen
        super().update(camera_x)