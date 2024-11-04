import pygame
from .Platform import Platform

class PlatformManager:
    def __init__(self, all_sprites, surface, tile_size=32):
        self.all_sprites = all_sprites
        self.platforms = pygame.sprite.Group()
        self.surface = surface
        self.tile_size = tile_size
    
    def create_platforms_from_map(self, tilemap):
        # Clear existing platforms
        for platform in self.platforms:
            platform.kill()
        
        # Create new platforms from tilemap
        for row in range(len(tilemap)):
            for col in range(len(tilemap[row])):
                tile_value = tilemap[row][col]
                if tile_value >= 0:  # Non-negative values represent platforms
                    platform = Platform(
                        self.all_sprites,
                        col * self.tile_size,  # x position
                        row * self.tile_size,  # y position
                        self.tile_size,        # width
                        self.tile_size,        # height
                        tile_value             # tile type
                    )
                    self.platforms.add(platform)
    
    def update(self, camera_x=0):
        for platform in self.platforms:
            platform.draw(self.surface, camera_x)