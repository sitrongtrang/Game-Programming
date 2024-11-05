import pygame
from classes.Items.BaseItem import BaseItem
from classes.Items.BulletItem import BulletItem
from classes.Items.DmgItem import DmgItem
from classes.Items.HealItem import HealItem
from classes.Items.SpeedItem import SpeedItem
from random import randint as _random 

class Shop(pygame.sprite.Sprite):
    class ShopKeeper():
        def __init__(self):
            self.items = {
                "Bullet": (BulletItem, 1),
                "Dmg": (DmgItem, 1),
                "Heal": (HealItem, 1),
                "Speed": (SpeedItem, 1)
            }

            self.shelf = []
            self.refresh_increase = 1
            self.refresh_cost = 1
            self.refresh_chance = 3

        def random_item(self, flag = True):
            _ : list
            if flag:
                _ = ["Bullet", "Dmg", "Heal", "Speed"]
            else:
                _ = ["Dmg", "Heal", "Speed"]
            return self.items.get(_[_random(0, len(_) - 1)])

        def sell_item(self, item: int):
            return self.shelf.pop(item % len(item))

        def init_shelf(self):
            # Always have a set of bullet when open shop
            self.shelf = [self.items["Bullet"], self.random_item(False) * 2]
        
        def refresh_shelf(self):
            self.shelf = [self.random_item()*3]
            cost = self.refresh_cost
            self.refresh_cost += self.refresh_increase
            self.refresh_chance -= 1
            return cost

        def can_refresh(self, player_coin):
            return self.refresh_chance > 0 and player_coin >= self.refresh_cost 

        def get_price(self, item_no: int):
            return self.shelf[item_no][1]

    def __init__(self, all_sprites, x, y, width, height):
        # Generic
        super().__init__()

        all_sprites.add(self)
        self.all_sprites = all_sprites

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0)) # Green color for placeholder

        # Rect attributes
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # Class specific 

        self.shopkeeper = Shop.ShopKeeper()
        self.shopkeeper.init_shelf()
        self.can_open = False

    def draw(self, screen, camera_x=0):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y, self.rect.width, self.rect.height))


    def sell_item(self, item_no: int): # 
        item, price = self.shopkeeper.sell_item(item_no)
        return self.create_item(item), price

    def create_item(self, item: BaseItem):
        return item(self.all_sprites, self.x, self.y, self.width, self.height)

    def can_buy(self, player_coin, item_no: int):
        return player_coin >= self.shopkeeper.get_price(item_no)
    
    def refresh_shop(self, player_coin):
        if self.shopkeeper.can_refresh(player_coin):
            return self.shopkeeper.refresh_shelf()
        return 0