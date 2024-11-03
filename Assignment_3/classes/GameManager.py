import pygame
from .CollisionManager import CollisionManager
from classes.Items.DmgItem import DmgItem
from classes.Characters.Player import Player
from classes.Characters.Enemy import Enemy
from classes.CollisionManager import CollisionManager
from classes.Coin import Coin
from classes.Platform import Platform
import random
from classes.Characters.Boss import Boss
class GameManager:
    # def __init__(self, screen, player, enemies, platforms, items, coins):
    def __init__(self, screen):
        self.screen = screen

    def new_game(self, level=""):
        if level != "":
            self.level = level
        # load self.level, implement later with tilemap
    
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        self.backgrounds = ["images/menu_background_image.png", "images/menu_background_image.png"]  # Replace with actual file paths
        self.bg_images = [pygame.image.load(bg).convert() for bg in self.backgrounds]

        # Calculate the total width of all background images combined
        self.total_bg_width = len(self.bg_images) * 800

        # Initialize player and add to all_sprites
        player = Player(self.all_sprites, 100, 550, 50, 50)
        enemy = Boss(self.all_sprites, 500, 550, 50, 50)
        self.enemies.add(enemy)

        # Platform settings
        platform_width, platform_height = 100, 20
        for _ in range(5):
            platform_x = random.randint(0, self.total_bg_width - platform_width)
            platform_y = random.randint(600 // 2, 600 - platform_height)
            platform = Platform(self.all_sprites, platform_x, platform_y, platform_width, platform_height)
            self.platforms.add(platform)
        
        self.camera_x = 0

        item = DmgItem(self.all_sprites, 400, 550, 50, 50)
        self.items.add(item)

        coin = Coin(self.all_sprites, 370, 270, 20, 20)
        self.coins.add(coin)

        self.player = player
        self.collision_manager = CollisionManager(self)
        self.player_coins = 0
    
    def update(self):
        self.player.rect.x = max(0, min(self.player.rect.x, self.total_bg_width - 50))
        self.camera_x = max(0, min(self.player.rect.x - 800 // 2, self.total_bg_width - 800))
        for i, bg_image in enumerate(self.bg_images):
            bg_x = i * 800
            self.screen.blit(bg_image, (bg_x - self.camera_x, 0))
        self.all_sprites.update()
        for sprite in self.all_sprites:
            if sprite.image:
                self.screen.blit(sprite.image, (sprite.rect.x - self.camera_x, sprite.rect.y, sprite.rect.width, sprite.rect.height))
        self.collision_manager.update()