import pygame

class CollisionManager:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def check_bullet_collisions(self):
        # Check for collisions between player bullets and enemies
        for bullet in self.player.bullets:
            hit_enemies = pygame.sprite.spritecollide(bullet, self.enemies, False)
            for enemy in hit_enemies:
                enemy.take_damage(1)
                bullet.kill()  # Destroy bullet upon collision

        # Check for collisions between enemy bullets and player
        for enemy in self.enemies:
            for bullet in enemy.bullets:  # Assuming each enemy has a 'bullets' list
                if bullet.rect.colliderect(self.player.rect):
                    self.player.take_damage(1)
                    bullet.kill()  # Destroy bullet upon collision

    def check_sword_collisions(self):
        # Check for collisions between player's sword and enemies
        if self.player.sword_hitbox:
            for enemy in self.enemies:
                if self.player.sword_hitbox.colliderect(enemy.rect):
                    enemy.take_damage(1)

        # Check for collisions between enemy swords and player
        for enemy in self.enemies:
            if enemy.sword_hitbox and enemy.sword_hitbox.colliderect(self.player.rect):
                self.player.take_damage(1)
    def update(self):
        self.check_bullet_collisions()
        self.check_sword_collisions()
