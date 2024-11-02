import pygame
from .CollisionManager import CollisionManager
from classes.Items.DmgItem import DmgItem
from classes.Characters.Player import Player
from classes.Characters.Enemy import Enemy
from classes.CollisionManager import CollisionManager
from classes.Coin import Coin
from classes.Characters.Boss import Boss
class GameManager:
    # def __init__(self, screen, player, enemies, platforms, items, coins):
    def __init__(self, screen):
        self.screen = screen

    def new_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # Initialize player and add to all_sprites
        player = Player(self.all_sprites, 100, 550, 50, 50)
        enemy = Boss(self.all_sprites, 500, 550, 50, 50)
        self.enemies.add(enemy)

        # Platform settings
        platform_width, platform_height = 100, 20
        platforms = [
            pygame.Rect(200, 450, platform_width, platform_height),
            pygame.Rect(350, 300, platform_width, platform_height)
        ]

        item = DmgItem(400, 550, 50, 50)
        items = [item]

        coin = Coin(370, 270, 20, 20)
        coins = [coin]

        self.player = player
        self.platforms = platforms
        self.items = items
        self.coins = coins
        self.collision_manager = CollisionManager(player, self.enemies, platforms, items, coins, self)
        self.player_coins = 0
    
    def update(self):
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)
        for platform in self.platforms:
            pygame.draw.rect(self.screen, (150, 75, 0), platform)
        for item in self.items:
            item.update(self.screen, self.items)
        for coin in self.coins:
            coin.update(self.screen)
        self.collision_manager.update()