import pygame
from .Character import Character


class Player(Character):
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
            self.sword_hitbox = pygame.Rect(sword_x, self.rect.y + 10, 400, 20)  # Adjusted size
            self.sword_timer = self.sword_duration

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if self.has_gun and current_time - self.last_shot_time >= self.gun_speed:
            bullet = Bullet(self.all_sprites,self.rect.centerx, self.rect.top, self.direction)
            self.bullets.add(bullet)  # Add to bullet group
            self.last_shot_time = current_time

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move_left()
            self.direction = "left"  # Set player direction
        if keys[pygame.K_d]:
            self.move_right()
            self.direction = "right"  # Set player direction
        if keys[pygame.K_w]:
            self.jump()
        if keys[pygame.K_m]:  # Sword attack key
            self.sword_attack()
        if keys[pygame.K_n]:  # Shoot key
            self.shoot()

    def update(self):
        super().update()  # Update movement and gravity from Character class
        self.handle_keys()
        self.bullets.update()  # Update bullets

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

    def check_sword_collisions(self, enemies):
        # Check for collisions with enemies
        if self.sword_hitbox:
            hit_enemies = [enemy for enemy in enemies if self.sword_hitbox.colliderect(enemy.rect)]
            for enemy in hit_enemies:
                enemy.take_damage(1)  # Assuming enemies have a take_damage method


class Bullet(pygame.sprite.Sprite):
    def __init__(self,all_sprites, x, y, direction="right"):
        super().__init__()
        self.all_sprites = all_sprites
        all_sprites.add(self)
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 0, 0))  # Red color for bullets
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 1 if direction == "right" else -1  # Set speed based on direction

    def update(self):
        self.rect.x += self.speed  # Move bullet in the set direction
        # Remove bullet if it goes off screen
        if self.rect.x > 800 or self.rect.x < 0:
            self.kill()
