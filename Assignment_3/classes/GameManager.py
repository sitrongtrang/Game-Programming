import pygame
from .CollisionManager import CollisionManager
from classes.Items.DmgItem import DmgItem
from classes.Characters.Player import Player
from classes.Characters.Enemy import Enemy
from classes.CollisionManager import CollisionManager
from classes.Coin import Coin
import random

class GameManager:
    # def __init__(self, screen, player, enemies, platforms, items, coins):
    def __init__(self, screen):
        self.screen = screen

    def new_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.backgrounds = ["images/menu_background_image.png", "images/menu_background_image.png"]  # Replace with actual file paths
        self.bg_images = [pygame.image.load(bg).convert() for bg in self.backgrounds]

        # Calculate the total width of all background images combined
        self.total_bg_width = len(self.bg_images) * 800

        # Initialize player and add to all_sprites
        player = Player(self.all_sprites, 100, 550, 50, 50)
        enemy = Enemy(self.all_sprites, 500, 550, 50, 50)
        self.enemies.add(enemy)

        # Platform settings
        platform_width, platform_height = 100, 20
        self.platforms = []
        for i in range(5):
            platform_x = random.randint(0, self.total_bg_width - platform_width)
            platform_y = random.randint(600 // 2, 600 - platform_height)
            self.platforms.append(pygame.Rect(platform_x, platform_y, platform_width, platform_height))
        
        self.camera_x = 0

        item = DmgItem(400, 550, 50, 50)
        items = [item]

        coin = Coin(370, 270, 20, 20)
        coins = [coin]

        self.player = player
        # self.platforms = platforms
        self.items = items
        self.coins = coins
        self.collision_manager = CollisionManager(self)
        self.player_coins = 0
    
    def update(self):
        self.player.rect.x = max(0, min(self.player.rect.x, self.total_bg_width - 50))
        self.camera_x = max(0, min(self.player.rect.x - 800 // 2, self.total_bg_width - 800))
        for i, bg_image in enumerate(self.bg_images):
            bg_x = i * 800
            self.screen.blit(bg_image, (bg_x - self.camera_x, 0))
        self.all_sprites.update()
        # self.all_sprites.draw(self.screen)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, (sprite.rect.x - self.camera_x, sprite.rect.y, sprite.rect.width, sprite.rect.height))
        for platform in self.platforms:
            pygame.draw.rect(self.screen, (150, 75, 0), (platform.x - self.camera_x, platform.y, platform.width, platform.height))
        for item in self.items:
            item.update(self.screen, self.items, self.camera_x)
        for coin in self.coins:
            coin.update(self.screen, self.camera_x)
        self.collision_manager.update()