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
from .MapSpawner import MapSpawner
from data import constant
from .PlatformManager import PlatformManager

class GameManager:
    # def __init__(self, screen, player, enemies, platforms, items, coins):
    def __init__(self, screen):
        self.screen = screen

    def level_string_to_level_id(self, level_string):
        chapter, level = level_string.split('-')
    
        chapter = int(chapter)
        level = int(level)
        
        level_id = chapter * 10 + level - 1
        
        return level_id

    def new_game(self, level=""):
        if level != "":
            self.level = level

        self.all_sprites = pygame.sprite.Group()

        level_id = self.level_string_to_level_id(self.level)
        self.mapSpawner = MapSpawner(self.screen, level_id)
        self.mapSpawner.spawnMap(0)

        self.platform_manager = PlatformManager(self.all_sprites, self.screen)
        self.platform_manager.create_platforms_from_map(self.mapSpawner.tilemap.map)

        self.player = None
        self.boss = None
        self.player_is_dead = False
        self.boss_is_dead = False
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.platforms = self.platform_manager.platforms

        # if self.tile_map.player_position:
        #     player_x, player_y = self.tile_map.player_position
        #     self.player = Player(self.all_sprites, player_x, player_y, constant.TILE_SIZE, constant.TILE_SIZE)
        
        # if self.tile_map.boss_position:
        #     boss_x, boss_y = self.tile_map.boss_position
        #     self.boss = Boss(self.all_sprites, boss_x, boss_y, constant.TILE_SIZE, constant.TILE_SIZE)
        #     self.enemies.add(self.boss)

        # # Initialize Enemies
        # for enemy_pos in self.tile_map.enemy_positions:
        #     enemy_x, enemy_y = enemy_pos
        #     enemy = Enemy(self.all_sprites, enemy_x, enemy_y, constant.TILE_SIZE, constant.TILE_SIZE)
        #     self.enemies.add(enemy)

        # # Initialize Platforms
        # for platform_pos in self.tile_map.platform_positions:
        #     platform_x, platform_y = platform_pos
        #     platform = Platform(self.all_sprites, platform_x, platform_y, constant.TILE_SIZE, constant.TILE_SIZE)
        #     self.platforms.add(platform)

        # # Initialize Items
        # for item_pos in self.tile_map.item_positions:
        #     item_x, item_y = item_pos
        #     item = DmgItem(self.all_sprites, item_x, item_y, constant.TILE_SIZE, constant.TILE_SIZE)
        #     self.items.add(item)

        # # Initialize Coins
        # for coin_pos in self.tile_map.coin_positions:
        #     coin_x, coin_y = coin_pos
        #     coin = Coin(self.all_sprites, coin_x, coin_y, constant.TILE_SIZE, constant.TILE_SIZE)
        #     self.coins.add(coin)

        self.player = Player(self.all_sprites, 100, 300, 32, 32)
        self.boss = Boss(self.all_sprites, 1000, 300, 50, 50)
        self.enemies.add(self.boss)

        self.total_bg_width = len(self.mapSpawner.backgroundFolders) * constant.SCREEN_WIDTH

        self.collision_manager = CollisionManager(self)
        self.player_coins = 0
    
    def update(self):
        self.player.rect.x = max(0, min(self.player.rect.x, self.total_bg_width - self.player.rect.width))
        self.camera_x = max(0, min(self.player.rect.x - constant.SCREEN_WIDTH // 2, self.total_bg_width - constant.SCREEN_WIDTH))
        self.mapSpawner.renderMap(self.camera_x)
        for sprite in self.all_sprites:
            sprite.draw(self.screen, self.camera_x)
        if self.platform_manager:
            self.platform_manager.update(self.camera_x)
        self.all_sprites.update(self.camera_x)
        self.collision_manager.update()
        self.player_is_dead = self.player not in self.all_sprites
        self.boss_is_dead = self.boss not in self.all_sprites