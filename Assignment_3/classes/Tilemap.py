import pygame, csv, os
import numpy as np
from classes.Tileset import Tileset
from data import constant

class Tilemap:
    def __init__(self, tileSetFile, mapFile, size=(30, 20), screenSize=(800, 600)):
        self.size = size
        self.tileSetFile = tileSetFile
        self.map = self.read_csv(mapFile)
        self.tileset = Tileset(tileSetFile)
        
        # Calculate the total map width in pixels
        self.map_width = self.map.shape[1] * 32  # 32 is tile size
        self.map_height = self.map.shape[0] * 32
        
        # Create a surface large enough for the entire map with alpha channel
        self.image = pygame.Surface((self.map_width, self.map_height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        
        # Store background information
        self.backgrounds = []
        self.parallax_factors = [0.2, 0.4, 0.6, 0.8, 1.0]  # Adjust for different scroll speeds
        
        # Create a mask surface to track transparent areas
        self.tile_mask = pygame.Surface((self.map_width, self.map_height), pygame.SRCALPHA)
        self.tile_mask.fill((0, 0, 0, 0))  # Initialize as fully transparent
    
    def renderMap(self, backgrounds):
        self.backgrounds = backgrounds
        # Render the initial state of the map
        self.drawInitialMap()
    
    def drawInitialMap(self):
        # Clear the surfaces
        self.image.fill((0, 0, 0, 0))
        self.tile_mask.fill((0, 0, 0, 0))
        
        # Draw tiles
        m, n = self.map.shape
        for i in range(m):
            for j in range(n):
                if self.map[i, j] != -1:  # Only draw non-transparent tiles
                    tile = self.tileset.tiles[self.map[i, j]]
                    # Draw tile on both the main image and mask
                    self.image.blit(tile, (j*32, i*32))
                    # Add an opaque rectangle to the mask where we have tiles
                    pygame.draw.rect(self.tile_mask, (255, 255, 255, 255), (j*32, i*32, 32, 32))
    
    def render(self, surface: pygame.Surface, camera_x: int):
        # Calculate visible area
        screen_width = surface.get_width()
        screen_height = surface.get_height()
        
        # Create a temporary surface for this frame
        temp_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        
        # Render backgrounds with parallax
        for i, bg in enumerate(self.backgrounds):
            # Calculate parallax offset
            parallax_factor = self.parallax_factors[i % len(self.parallax_factors)]
            bg_offset = -(camera_x * parallax_factor)
            
            # Calculate how many times we need to tile the background
            bg_width = bg.get_width()
            tiles_needed = (screen_width // bg_width) + 2
            
            # Draw background tiles
            for tile in range(tiles_needed):
                x_pos = bg_offset + (tile * bg_width)
                if -bg_width < x_pos < screen_width:
                    temp_surface.blit(bg, (x_pos, 0))
        
        # Calculate the visible portion of the tilemap
        visible_area = pygame.Rect(
            camera_x, 0,
            min(screen_width, self.map_width - camera_x),
            min(screen_height, self.map_height)
        )
        
        # Get the visible portion of the tile mask
        visible_mask = pygame.Surface((visible_area.width, visible_area.height), pygame.SRCALPHA)
        visible_mask.blit(self.tile_mask, (0, 0), visible_area)
        
        # Draw the visible portion of the tilemap onto the temporary surface
        temp_surface.blit(self.image, (0, 0), visible_area)
        
        # Finally, draw the completed frame to the main surface
        surface.blit(temp_surface, (0, 0))
    
    def read_csv(self, fileName):
        map_data = []
        with open(os.path.join(fileName)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map_data.append(list(map(int, row)))
        return np.array(map_data)

    def __str__(self):
        return f'{self.__class__.__name__} {self.size}'      