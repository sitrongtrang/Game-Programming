import pygame
from data import constant

class Character(pygame.sprite.Sprite):
    def __init__(self,all_sprites, x, y, width, height, gravity=1):
        super().__init__()

        all_sprites.add(self)
        self.all_sprites = all_sprites

        self.hp = constant.PLAYER_HP
        # Placeholder sprite
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 255))  # Green color for placeholder

        # Rect attributes
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Movement attributes
        self.speed = constant.PLAYER_SPEED
        self.jump_power = constant.JUMP_POWER
        self.gravity = gravity
        self.vel_y = 0
        self.is_jumping = False

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

    def jump(self):
        if not self.is_jumping:
            self.vel_y = -self.jump_power
            self.is_jumping = True

    def apply_gravity(self):
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # Ground collision
        if self.rect.y >= constant.GROUND_LEVEL:
            self.rect.y = constant.GROUND_LEVEL
            self.is_jumping = False
            self.vel_y = 0

    def update(self):
        self.apply_gravity()

    def take_damage(self,dame):
        self.hp-=dame
        if self.hp <= 0:
            self.kill()