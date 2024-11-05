import pygame
from classes.Characters.Boss import Boss
from classes.Items.DmgItem import DmgItem
from classes.Characters.Player import Player
from classes.Characters.Enemy import Enemy
from classes.Characters.Bullet import *
from .Coin import Coin
from .CollisionManager import CollisionManager
from .MapSpawner import MapSpawner
from data import constant
from .PlatformManager import PlatformManager
from classes.Characters.Barrel import Barrel
from classes.Items.BulletItem import BulletItem
from .Shop import Shop
import json

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
        self.barrels = pygame.sprite.Group()
        self.platforms = self.platform_manager.platforms

        with open("data/levels/" + self.level + ".json", 'r') as f:
            self.entities = json.load(f)

        player_data = self.entities['Player']
        coins_data = self.entities['Coins']
        enemies_data = self.entities['Enemies']
        boss_data = self.entities['Boss']
        barrels_data = self.entities['Barrels']
        bullets_data = self.entities['BulletItems']
        shop_data = self.entities['Shop']

        if player_data:
            self.player = Player(self.all_sprites, player_data['x'], player_data['y'], 32, 32)

        # for coin_data in coins_data:
        #     coin = Coin(self.all_sprites, coin_data['x'], coin_data['y'], 32, 32)
        #     self.coins.add(coin)

        # for enemy_data in enemies_data:
        #     enemy = Enemy(self.all_sprites, enemy_data['x'], enemy_data['y'], 32, 32)
        #     self.enemies.add(enemy)

        if boss_data:
            self.boss = Boss(self.all_sprites, boss_data['x'], boss_data['y'], 32, 32)
            self.enemies.add(self.boss)

        # for barrel_data in barrels_data:
        #     barrel = Barrel(self.all_sprites, barrel_data['x'], barrel_data['y'])
        #     self.barrels.add(barrel)

        # for bullet_data in bullets_data:
        #     bullet = BulletItem(self.all_sprites, bullet_data['x'], bullet_data['y'], 32, 32)
        #     self.items.add(bullet)

        if shop_data:
            self.shop = Shop(self.all_sprites, shop_data['x'], shop_data['y'], 64, 64)
        

        self.boss = Boss(self.all_sprites, 1000, 300, 1000, 1000)
        barrels = [(10, 30), (600, 300), (700, 300), (800, 300), (900, 300)]
        enemy = Enemy(self.all_sprites, 300, 300, 48, 48) 

        self.enemies.add(enemy) 
        self.enemies.add(self.boss)
        for barrels in barrels:
            self.barrels.add(Barrel(self.all_sprites, *barrels))
        # self.total_bg_width = len(self.mapSpawner.backgroundFolders) * constant.SCREEN_WIDTH
        self.total_bg_width = self.mapSpawner.tilemap.map_width

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