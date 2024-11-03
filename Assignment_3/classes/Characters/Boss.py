import pygame
from .Enemy import Enemy
from .Bullet import Bullet_Player
from data import constant

class Boss(Enemy):
    def __init__(self, all_sprites, x, y, width, height):
        super().__init__(all_sprites, x, y, width, height, constant.BOSS_RANGE)
        # Customize boss-specific attributes
        self.hp = constant.BOSS_HP  # Higher HP for the boss
        self.damage = constant.BOSS_DMG  # Higher damage for the boss
        self.speed = constant.BOSS_SPEED  # Adjusted speed for boss
        self.special_attack_timer = 0
        self.special_attack_cooldown = 2000  # Cooldown in milliseconds for special attack
        self.last_special_attack_time = 0  # Track the last special attack time
        self.is_enraged = False  # Boss enrages at low HP
        self.image.fill((255, 255, 0))  # Color the boss yellow
        # Sword attack attributes
        self.sword_hitbox = None
        self.sword_duration = 50  # Duration in frames for sword hitbox visibility
        self.sword_timer = 0
        self.sword_delay = 300  # Delay in milliseconds after special attack
        self.direction = "left"  # Initial direction of boss

    def sword_attack(self):
        # Create a temporary hitbox in front of the boss
        if self.sword_timer == 0:  # Only create if there's no active sword hitbox
            sword_x = self.rect.right if self.direction == "right" else self.rect.left - 40
            self.sword_hitbox = pygame.Rect(sword_x, self.rect.y + 10, 40, 20)  # Adjusted size
            self.sword_timer = self.sword_duration
            print("boss sword attack")

    def special_attack(self):
        # Boss-specific powerful attack logic
        current_time = pygame.time.get_ticks()
        if current_time - self.special_attack_timer >= self.special_attack_cooldown:
            # Trigger a unique attack, like shooting multiple bullets in different directions
            for angle in range(0, 360, 45):
                bullet = Bullet_Player(self.all_sprites, self.rect.centerx, self.rect.centery, angle)
                self.bullets.add(bullet)
            self.special_attack_timer = current_time
            self.last_special_attack_time = current_time  # Update last special attack time

    def update(self, camera_x=0):
        super().update(camera_x)  # Use the update logic from Enemy
        self.special_attack()  # Call the special attack function

        # Trigger enrage mode if HP is below a threshold
        if self.hp < constant.BOSS_HP * 0.3 and not self.is_enraged:
            self.is_enraged = True
            self.speed *= 1.5  # Increase speed when enraged
            self.gun_speed *= 0.5  # Decrease gun cooldown for faster shooting

        # Check if it's time to perform a delayed sword attack after special attack
        current_time = pygame.time.get_ticks()
        if current_time - self.last_special_attack_time >= self.sword_delay and self.last_special_attack_time > 0:
            self.sword_attack()
            self.last_special_attack_time = 0  # Reset to avoid repeated attacks

        # Update sword timer and deactivate hitbox when time runs out
        if self.sword_timer > 0:
            self.sword_timer -= 1
        else:
            self.sword_hitbox = None  # Remove sword hitbox after duration

    def should_sword_attack(self):
        # Placeholder function to determine when the boss should use a sword attack
        return True  # Always return True for testing purposes
