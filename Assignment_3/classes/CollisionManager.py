import pygame

class CollisionManager:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def check_bullet_collisions(self):
        # Check for collisions between bullets and enemies
        for bullet in self.player.bullets:
            hit_enemies = pygame.sprite.spritecollide(bullet, self.enemies, False)
            for enemy in hit_enemies:
                enemy.take_damage(1)  # Assuming enemies have a take_damage method
                bullet.kill()  # Destroy bullet upon collision

    def check_sword_collisions(self):
        # Check for collisions between sword hitbox and enemies
        if self.player.sword_hitbox:
            for enemy in self.enemies:
                if self.player.sword_hitbox.colliderect(enemy.rect):
                    enemy.take_damage(1)  # Apply damage on collision

    def update(self):
        self.check_bullet_collisions()
        self.check_sword_collisions()
