import pygame
from .Character import Character

class Player(Character):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        # Additional attributes for patrolling and shooting
        self.patrol_speed = 2
        self.patrol_direction = 1  # 1 for right, -1 for left
        self.patrol_distance = 100  # pixels to patrol before turning
        self.patrol_start_x = x  # starting x-coordinate for patrol
        self.has_gun = True  # Indicates if the player has a gun
        self.bullets = pygame.sprite.Group()

    def patrol(self):
        # Moves left and right within patrol range
        self.rect.x += self.patrol_speed * self.patrol_direction
        if abs(self.rect.x - self.patrol_start_x) >= self.patrol_distance:
            self.patrol_direction *= -1  # Change direction

    def shoot(self):
        if self.has_gun:
            # Create a bullet at the player's position
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.bullets.add(bullet)

    def update(self):
        super().update()  # Update movement and gravity from Character class
        # self.patrol()  # Perform patrolling behavior

        # Update bullets
        # self.bullets.update()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 0, 0))  # Red color for bullets
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10

    def update(self):
        self.rect.x += self.speed  # Bullet moves to the right
        # Remove bullet if it goes off screen
        if self.rect.x > 800:
            self.kill()
