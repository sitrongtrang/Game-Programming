import pygame
import math
from .Character import Character
from .Bullet import *
from data import constant

class Player(Character):
    def __init__(self, all_sprites, x, y, width, height):
        super().__init__(all_sprites, x, y, width, height, constant.PLAYER_HP, constant.PLAYER_DMG, constant.PLAYER_SPEED)
        # Attributes for attacking
        self.has_gun = True  # Indicates if the player has a gun
        self.gun_speed = 500  # Cooldown in milliseconds for shooting
        self.last_shot_time = 0  # Track last shot time
        self.bullets = pygame.sprite.Group()
        self.sword_hitbox = None  # Placeholder for sword attack hitbox
        self.sword_duration = 50  # Duration in frames for sword hitbox visibility
        self.sword_timer = 0
        self.direction = "right"

        # Init Animations
        self.setup_animations()

    def setup_animations(self):
        self.animator.add_animation("idle_left", 'assets\\animations\\character\\idle_left.png', (32, 36), 4, 0.2)
        self.animator.add_animation("idle_right", 'assets\\animations\\character\\idle_right.png', (32, 36), 4, 0.2)
        self.animator.add_animation("run_left", 'assets\\animations\\character\\run_left.png', (32, 32), 5, 0.2, 16)
        self.animator.add_animation("run_right", 'assets\\animations\\character\\run_right.png', (32, 32), 5, 0.2, 16)
        self.animator.add_animation("jump_right", 'assets\\animations\\character\\jump_right.png', (32, 48), 4, 0.7,16, False)
        self.animator.add_animation("jump_left", 'assets\\animations\\character\\jump_left.png', (32, 48), 4, 0.7, 16, False)
        self.animator.add_animation("melee_left", 'assets\\animations\\character\\melee_left.png', (32, 48), 6, 0.1, 16, False)
        self.animator.add_animation("melee_right", 'assets\\animations\\character\\melee_right.png', (32, 48), 6, 0.1, 16, False)
        #
        self.setAnim("idle")

    def check_animInteval(self):
      
        if self.sword_timer > 0:

            return False
        if self.is_jumping:
            return False
        return True

    def sword_attack(self):
        # Create a temporary hitbox in front of the player
        if self.sword_timer == 0:  # Only create if there's no active sword hitbox
            sword_x = self.rect.right if self.direction == "right" else self.rect.left - 40
            self.sword_hitbox = pygame.Rect(sword_x, self.rect.y + 10, 40, 20)  # Adjusted size
            self.setAnim("melee")
            self.sword_timer = self.sword_duration
            

    def shoot(self, camera_x=0):
        current_time = pygame.time.get_ticks()
        mouse_buttons = pygame.mouse.get_pressed()

        if self.has_gun and mouse_buttons[2] and current_time - self.last_shot_time >= self.gun_speed and self.bullet > 0:
            self.bullet -= 1
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Update player direction based on mouse position
            self.direction = "right" if mouse_x > self.rect.centerx else "left"

            # Calculate angle toward the mouse position
            direction_x = mouse_x - self.rect.centerx + camera_x
            direction_y = mouse_y - self.rect.centery
            angle = math.atan2(direction_y, direction_x)

            # Create bullet heading toward the mouse position with updated direction
            bullet = Bullet_Player(self.all_sprites, self.rect.centerx, self.rect.centery, angle, self.direction)
            self.bullets.add(bullet)
            self.last_shot_time = current_time

    def handle_keys(self):
        keys = pygame.key.get_pressed()

        # Check for horizontal movement
        if keys[pygame.K_a]:
            self.move_left()
            self.direction = "left"  # Set player direction
            self.setAnim("run")
        elif keys[pygame.K_d]:
            self.move_right()
            self.direction = "right"  # Set player direction
            self.setAnim("run")
        else:
            self.stop()  # Stop horizontal movement if neither left nor right is pressed
            self.setAnim("idle")

        # Check for jumping
        if keys[pygame.K_w]:
            self.jump()
            self.setAnim("jump")

        # Sword attack
        if pygame.mouse.get_pressed()[0]:  # Index 2 represents the right mouse button
            self.sword_attack()

    def update(self, camera_x=0):
        super().update(camera_x)  # Update movement and gravity from Character class
        self.handle_keys()

        # Check for mouse button press to shoot
        self.shoot(camera_x)  # Call shoot method on update

        self.bullets.update(camera_x)  # Update bullets

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
