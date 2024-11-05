import pygame

class CollisionManager:
    def __init__(self, game_manager):
        self.game_manager = game_manager

    def check_bullet_collisions(self):
        # Check for collisions between player bullets and enemies
        for bullet in self.player.bullets:
            hit_enemies = pygame.sprite.spritecollide(bullet, self.enemies, False)
            for enemy in hit_enemies:
                enemy.take_damage(self.player.dmg)
                bullet.kill()  # Destroy bullet upon collision

        # Check for collisions between enemy bullets and player
        for enemy in self.enemies:
            for bullet in enemy.bullets:  # Assuming each enemy has a 'bullets' list
                if bullet.rect.colliderect(self.player.rect):
                    self.player.take_damage(enemy.dmg)
                    bullet.kill()  # Destroy bullet upon collision

    def check_bullet_platform_collisions(self):
        # Check for collisions between player bullets and platforms
        for bullet in self.player.bullets:
            for platform in self.platforms:
                if bullet.rect.colliderect(platform):  # Remove '.rect' from platform
                    bullet.kill()  # Destroy bullet upon collision with platform
                for barrel in self.barrels:
                    if bullet.rect.colliderect(barrel):
                        barrel.destroy()
                        bullet.kill()

        # Check for collisions between enemy bullets and platforms
        for enemy in self.enemies:
            for bullet in enemy.bullets:
                for platform in self.platforms:
                    if bullet.rect.colliderect(platform):  # Remove '.rect' from platform
                        bullet.kill()  # Destroy bullet upon collision with platform
                for barrel in self.barrels:
                    if bullet.rect.colliderect(barrel):
                        barrel.destroy()
                        bullet.kill()

    def check_sword_collisions(self):
        # Check for collisions between player's sword and enemies
        if self.player.sword_hitbox and self.player.sword_hitbox[1]:
            for enemy in self.enemies:

                if self.player.sword_hitbox[0].colliderect(enemy.rect):
                    enemy.take_damage(self.player.dmg)
            self.player.sword_hitbox[1] = False  # Deactivate sword hitbox

        # Check for collisions between enemy swords and player
        for enemy in self.enemies:
            # with enemy.sword_hitbox as hitbox:
            if enemy.sword_hitbox and enemy.sword_hitbox[1] \
                and enemy.sword_hitbox[0].colliderect(self.player.rect):
                self.player.take_damage(self.player.dmg)
                enemy.sword_hitbox[1] = False  # Deactivate enemy sword hitbox

    def character_platform_collisions(self, char):
        for platform in self.platforms:
            if char.rect.colliderect(platform):
                # Buffer to reduce overlapping issues
                buffer = 1

                # Vertical collision: Check if character is falling onto the platform
                if char.vel_y > 0 and char.rect.bottom <= platform.rect.top + char.vel_y:
                    char.rect.bottom = platform.rect.top
                    char.vel_y = 0
                    char.is_jumping = False

                # Vertical collision: Check if character hits the bottom of a platform while moving up
                elif char.vel_y < 0 and char.rect.top >= platform.rect.bottom + char.vel_y - buffer:
                    char.rect.top = platform.rect.bottom
                    char.vel_y = 0

                # Horizontal collision: Check if character hits the left side of the platform
                elif char.vel_x > 0 and char.rect.right <= platform.rect.left + char.vel_x:
                    char.rect.right = platform.rect.left
                    char.vel_x = 0

                # Horizontal collision: Check if character hits the right side of the platform
                elif char.vel_x < 0 and char.rect.left >= platform.rect.right + char.vel_x:
                    char.rect.left = platform.rect.right
                    char.vel_x = 0

    def check_platform_collisions(self):
        for enemy in self.enemies:
            self.character_platform_collisions(enemy)
        self.character_platform_collisions(self.player)

    def character_item_collisions(self, char):
        for item in self.items:
            if item.image and char.rect.colliderect(item.rect):
                item.pickedUp(char)

    def character_coin_collisions(self, char):
        for coin in self.coins:
            if char.rect.colliderect(coin.rect):
                self.game_manager.player_coins += 1
                coin.kill()

    def check_player_enemy_collisions(self):
        # Check for collisions between player and enemies
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                # Check if the player is landing on top of the enemy
                if self.player.vel_y > 0 and self.player.rect.bottom <= enemy.rect.top + abs(self.player.vel_y):
                    # Player is stomping on the enemy
                    # enemy.take_damage(self.player.dmg)  # Enemy takes damage
                    self.player.vel_y = -10  # Bounce player up after stomp
                else:
                    # Handle side or head collisions (player takes damage)
                    # self.player.take_damage(enemy.dmg)
                    # Optional: knock back the player or enemy
                    if self.player.rect.centerx < enemy.rect.centerx:
                        self.player.rect.x -= 10  # Knock player back to the left
                    else:
                        self.player.rect.x += 10  # Knock player back to the right

    def check_player_shop_collisions(self, char):
        # Check for collisions between player and shop
        if not self.player.rect.colliderect(self.shop.rect):
            return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            player_coin = self.game_manager.player_coins
            item_no = 0
            if self.shop.can_buy(player_coin, item_no):
                item, price = self.shop.sell_item(item_no)
                self.game_manager.player_coins -= price
                item.pickedUp(char)
        elif keys[pygame.K_2]:
            player_coin = self.game_manager.player_coins
            item_no = 1
            if self.shop.can_buy(player_coin, item_no):
                item, price = self.shop.sell_item(item_no)
                self.game_manager.player_coins -= price
                item.pickedUp(char)
        elif keys[pygame.K_3]:
            player_coin = self.game_manager.player_coins
            item_no = 2
            if self.shop.can_buy(player_coin, item_no):
                item, price = self.shop.sell_item(item_no)
                self.game_manager.player_coins -= price
                item.pickedUp(char)
        elif keys[pygame.K_r]:
            player_coin = self.game_manager.player_coins
            cost = self.shop.refresh_shop(player_coin)
            self.game_manager.player_coins -= cost


    def update(self):
        self.player = self.game_manager.player
        self.enemies = self.game_manager.enemies
        self.platforms = self.game_manager.platforms
        self.items = self.game_manager.items
        self.coins = self.game_manager.coins
        self.barrels = self.game_manager.barrels
        self.shop = self.game_manager.shop
        self.check_bullet_collisions()
        self.check_sword_collisions()
        self.check_platform_collisions()
        self.character_item_collisions(self.player)
        self.character_coin_collisions(self.player)
        self.check_player_enemy_collisions()
        self.check_bullet_platform_collisions()
        self.check_player_shop_collisions(self.player)
