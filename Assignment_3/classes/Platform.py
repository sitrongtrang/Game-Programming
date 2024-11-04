import pygame
import os

class Platform(pygame.sprite.Sprite):
    def __init__(self, all_sprites, x, y, width, height, tile_type):
        super().__init__()
        
        all_sprites.add(self)
        self.all_sprites = all_sprites
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.tile_type = tile_type
        
        # Load the tileset image
        self.tileset_image = self.load_tileset()
        self.image = self.get_tile_image(tile_type)
        
        # Rect attributes
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def load_tileset(self):
        try:
            return pygame.image.load(os.path.join("assets", "maps", "tileset.png")).convert_alpha()
        except pygame.error as e:
            print(f"Could not load tileset: {e}")
            # Create a fallback colored surface if tileset loading fails
            fallback = pygame.Surface((32, 32))
            fallback.fill((150, 75, 0))
            return fallback
    
    def get_tile_image(self, tile_type):
        # Calculate tile position in tileset
        # Assuming tileset is arranged in rows with multiple columns
        TILE_SIZE = 32
        TILESET_COLUMNS = 12  # Adjust based on your tileset
        
        # Calculate row and column in tileset
        row = tile_type // TILESET_COLUMNS
        col = tile_type % TILESET_COLUMNS
        
        # Create a surface for the tile
        tile_surface = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
        
        # Copy the specific tile from tileset
        tile_rect = pygame.Rect(
            col * TILE_SIZE,
            row * TILE_SIZE,
            TILE_SIZE,
            TILE_SIZE
        )
        tile_surface.blit(self.tileset_image, (0, 0), tile_rect)
        
        return tile_surface
    
    def draw(self, screen, camera_x=0):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y, self.rect.width, self.rect.height))

