import pygame
from .Character import Character
from .Bullet import Bullet_Enemy
from data import constant


class Enemy(Character):
    def __init__(
        self, all_sprites, x, y, width, height, patrol_range=constant.PATROL_RANGE
    ):
        super().__init__(
            all_sprites,
            x,
            y,
            width,
            height,
            constant.ENEMY_HP,
            constant.ENEMY_DMG,
            constant.ENEMY_SPEED,
        )
        # Attributes for attacking
        #self.image.fill((255, 0, 0))
        self.has_gun = True  # Indicates if the player has a gun
        self.gun_speed = 1000  # Cooldown in milliseconds for shooting
        self.last_shot_time = 0  # Track last shot time
        self.bullets = pygame.sprite.Group()
        self.sword_hitbox = None  # Placeholder for sword attack hitbox
        self.sword_duration = 50  # Duration in frames for sword hitbox visibility
        self.sword_timer = 0
        self.direction = "right"

        self.patrol_range = patrol_range
        self.patrol_start = x - self.patrol_range
        self.patrol_end = x + self.patrol_range
        self.patrol_direction = 1

        self.lastDirection = self.direction
        self.setup_animations()

    def setup_animations(self):
        self.animator.add_animation("idle_left", 'assets\\animations\\enemy\\idle_left.png', (32, 48), 4, 0.2, 16)
        self.animator.add_animation("idle_right", 'assets\\animations\\enemy\\idle_right.png', (32, 48), 4, 0.2, 16)

        self.animator.add_animation("walk_left", 'assets\\animations\\enemy\\walk_left.png', (32, 48), 6, 0.2, 16)
        self.animator.add_animation("walk_right", 'assets\\animations\\enemy\\walk_right.png', (32, 48), 6, 0.2, 16)

        self.animator.add_animation("shoot_right", 'assets\\animations\\enemy\\shoot_right.png', (16*3, 48), 5, 0.02, 0, False)
        self.animator.add_animation("shoot_left", 'assets\\animations\\enemy\\shoot_left.png', (16*3, 48), 5, 0.02, 0, False)
        #
        self.setAnim("idle")

    def sword_attack(self):
        # Create a temporary hitbox in front of the player
        if self.sword_timer == 0:  # Only create if there's no active sword hitbox
            sword_x = (
                self.rect.right if self.direction == "right" else self.rect.left - 40
            )
            self.sword_hitbox = [pygame.Rect(
                sword_x, self.rect.y + 10, 40, 20
            ),True]  # Adjusted size
            self.sword_timer = self.sword_duration

    def patrol(self):
        if self.patrol_start == self.patrol_end:
            return
        if self.patrol_direction == 1 and self.rect.x >= self.patrol_end:
            self.patrol_direction = -1
            self.direction = "left"
        elif self.patrol_direction == -1 and self.rect.x <= self.patrol_start:
            self.patrol_direction = 1
            self.direction = "right"

        self.rect.x += self.patrol_direction * self.speed

        self.lastDirection = self.direction
        self.setAnim("walk")

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if self.has_gun and current_time - self.last_shot_time >= self.gun_speed:
            bullet = Bullet_Enemy(
                self.all_sprites, self.rect.centerx, self.rect.top, self.direction
            )
            self.bullets.add(bullet)  # Add to bullet group
            self.last_shot_time = current_time

            self.setAnim("shoot")

    def update(self, camera_x=0):
        super().update(camera_x)  # Update movement and gravity from Character class
        self.bullets.update(camera_x)  # Update bullets
        self.patrol()
        self.shoot()
        # Update sword timer and deactivate hitbox when time runs out
        if self.sword_timer > 0:
            self.sword_timer -= 1
        else:
            self.sword_hitbox = None  # Remove sword hitbox after duration

    def draw(self, surface, camera_x=0):
        # Draw the player character
        super().draw(surface, camera_x)  # Call the draw method from the Character class
        self.drawHpBar(surface, self.rect.x - camera_x - 15, self.rect.y - 25)
        # Draw sword hitbox if it's active
        if self.sword_hitbox:
            pass
            # pygame.draw.rect(
            #     surface,
            #     (0, 0, 255),
            #     (
            #         self.sword_hitbox[0].x - camera_x,
            #         self.sword_hitbox[0].y,
            #         self.sword_hitbox[0].width,
            #         self.sword_hitbox[0].height,
            #     ),
            # )  # Draw the sword hitbox in blue
