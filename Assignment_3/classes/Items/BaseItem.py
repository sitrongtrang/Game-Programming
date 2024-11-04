import pygame
from data import constant

class BaseItem(pygame.sprite.Sprite):
    def __init__(self, all_sprites, x, y, width, height):
        super().__init__()

        all_sprites.add(self)
        self.all_sprites = all_sprites

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.appear_duration = constant.ITEM_APPEAR_DUR
        self.effect_duration = constant.ITEM_EFFECT_DUR
        self.picked_up = False

        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))  # Green color for placeholder

        # Rect attributes
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.previous_ticks = pygame.time.get_ticks()
    
    def takeEffect(self, character):
        raise NotImplementedError
    
    def update(self, camera_x=0):
        deltaTime = pygame.time.get_ticks() - self.previous_ticks
        self.previous_ticks = pygame.time.get_ticks()
        if not self.picked_up:
            self.appear_duration -= deltaTime
            if self.appear_duration <= 0:
                self.kill()
        else:
            self.effect_duration -= deltaTime
            if self.effect_duration <= 0:
                self.kill()

    def pickedUp(self, character):
        self.image = None
        self.picked_up = True
        self.takeEffect(character)

    def draw(self, screen, camera_x=0):
        if self.image:
            screen.blit(self.image, (self.rect.x - camera_x, self.rect.y, self.rect.width, self.rect.height))

