import pygame
from .Character import Character
from .Bullet import Bullet_Enemy


class Enemy(Character):
    def __init__(self,all_sprites, x, y, width, height):
        super().__init__(all_sprites,x, y, width, height)
        # Attributes for attacking
        self.has_gun = True  # Indicates if the player has a gun
        self.gun_speed = 500  # Cooldown in milliseconds for shooting
        self.last_shot_time = 0  # Track last shot time
        self.bullets = pygame.sprite.Group()
        self.sword_hitbox = None  # Placeholder for sword attack hitbox
        self.sword_duration = 50  # Duration in frames for sword hitbox visibility
        self.sword_timer = 0
        self.direction = "right"

    def sword_attack(self):
        # Create a temporary hitbox in front of the player
        if self.sword_timer == 0:  # Only create if there's no active sword hitbox
            sword_x = self.rect.right if self.direction == "right" else self.rect.left - 40
            self.sword_hitbox = pygame.Rect(sword_x, self.rect.y + 10, 40, 20)  # Adjusted size
            self.sword_timer = self.sword_duration

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if self.has_gun and current_time - self.last_shot_time >= self.gun_speed:
            bullet = Bullet_Enemy(self.all_sprites,self.rect.centerx, self.rect.top, self.direction)
            self.bullets.add(bullet)  # Add to bullet group
            self.last_shot_time = current_time

    def update(self):
        super().update()  # Update movement and gravity from Character class
        self.bullets.update()  # Update bullets
        self.shoot()
        # Update sword timer and deactivate hitbox when time runs out
        if self.sword_timer > 0:
            self.sword_timer -= 1
        else:
            self.sword_hitbox = None  # Remove sword hitbox after duration

    def draw(self, surface):
        # Draw the player character
        super().draw(surface)  # Call the draw method from the Character class

        # Draw sword hitbox if it's active
        if self.sword_hitbox:
            pygame.draw.rect(surface, (0, 0, 255), self.sword_hitbox)  # Draw the sword hitbox in blue



