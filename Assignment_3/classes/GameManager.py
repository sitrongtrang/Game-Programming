import pygame
from classes.Characters.Boss import Boss
from classes.Items.DmgItem import DmgItem
from classes.Characters.Player import Player
from classes.Characters.Enemy import Enemy
from classes.Characters.Bullet import *
from .Coin import Coin
from .Platform import Platform
from .CollisionManager import CollisionManager
from .Tilemap import Tilemap
from data import constant

class GameManager:
    # def __init__(self, screen, player, enemies, platforms, items, coins):
    def __init__(self, screen):
        self.screen = screen

    def new_game(self, level=""):
        if level != "":
            self.level = level
        # load self.level, implement later with tilemap
        self.tile_map = Tilemap("", "data/levels/" + self.level + ".csv")
        self.tile_map.renderMap()

        self.player = None
        self.boss = None
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        if self.tile_map.player_position:
            player_x, player_y = self.tile_map.player_position
            self.player = Player(self.all_sprites, player_x, player_y, constant.TILE_SIZE, constant.TILE_SIZE)
        
        if self.tile_map.boss_position:
            boss_x, boss_y = self.tile_map.boss_position
            self.boss = Boss(self.all_sprites, boss_x, boss_y, constant.TILE_SIZE, constant.TILE_SIZE)
            self.enemies.add(self.boss)

        # Initialize Enemies
        for enemy_pos in self.tile_map.enemy_positions:
            enemy_x, enemy_y = enemy_pos
            enemy = Enemy(self.all_sprites, enemy_x, enemy_y, constant.TILE_SIZE, constant.TILE_SIZE)
            self.enemies.add(enemy)

        # Initialize Platforms
        for platform_pos in self.tile_map.platform_positions:
            platform_x, platform_y = platform_pos
            platform = Platform(self.all_sprites, platform_x, platform_y, constant.TILE_SIZE, constant.TILE_SIZE)
            self.platforms.add(platform)

        # Initialize Items
        for item_pos in self.tile_map.item_positions:
            item_x, item_y = item_pos
            item = DmgItem(self.all_sprites, item_x, item_y, constant.TILE_SIZE, constant.TILE_SIZE)
            self.items.add(item)

        # Initialize Coins
        for coin_pos in self.tile_map.coin_positions:
            coin_x, coin_y = coin_pos
            coin = Coin(self.all_sprites, coin_x, coin_y, constant.TILE_SIZE, constant.TILE_SIZE)
            self.coins.add(coin)

        self.backgrounds = ["images/menu_background_image.png", "images/menu_background_image.png"]  # Replace with actual file paths
        self.bg_images = [pygame.image.load(bg).convert() for bg in self.backgrounds]

        # Calculate the total width of all background images combined
        self.total_bg_width = len(self.bg_images) * constant.SCREEN_WIDTH

        self.collision_manager = CollisionManager(self)
        self.player_coins = 0
    
    def update(self):
        self.player.rect.x = max(0, min(self.player.rect.x, self.total_bg_width - self.player.rect.width))
        self.camera_x = max(0, min(self.player.rect.x - constant.SCREEN_WIDTH // 2, self.total_bg_width - constant.SCREEN_WIDTH))
        for i, bg_image in enumerate(self.bg_images):
            bg_x = i * constant.SCREEN_WIDTH
            self.screen.blit(bg_image, (bg_x - self.camera_x, 0))
        self.all_sprites.update(self.camera_x)
        for sprite in self.all_sprites:
            if sprite.image:
                self.screen.blit(sprite.image, (sprite.rect.x - self.camera_x, sprite.rect.y, sprite.rect.width, sprite.rect.height))
        self.collision_manager.update()