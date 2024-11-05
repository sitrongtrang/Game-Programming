import pygame
import os
from classes.Tilemap import Tilemap
from data import constant

class MapSpawner:
    def __init__(self, surface, mapNumber):
        self.surface = surface
        self.mapNumber = mapNumber
        
        self.mapFolders = [
            os.path.join("data", "maps", "1-1.csv")
        ]
        
        self.tileSetFolder = os.path.join("assets", "maps", "tileset.png")
        self.backgroundFolders = [
            os.path.join("assets", "maps", "Background1.png"),
            os.path.join("assets", "maps", "Background2.png"),
            os.path.join("assets", "maps", "Background1.png"),
            os.path.join("assets", "maps", "Background2.png"),
            os.path.join("assets", "maps", "Background1.png"),
            os.path.join("assets", "maps", "Background2.png"),
            os.path.join("assets", "maps", "Background1.png"),
            os.path.join("assets", "maps", "Background2.png"),
            os.path.join("assets", "maps", "Background1.png"),
            os.path.join("assets", "maps", "Background2.png"),
            
            # Add more background layers as needed
        ]
        
        self.backgrounds = []
        self.tilemap = None
        self.loadBackgrounds()
    
    def loadBackgrounds(self):
        self.backgrounds = []
        for bg_folder in self.backgroundFolders:
            try:
                bg_image = pygame.image.load(bg_folder).convert()
                scale_bg = pygame.transform.scale(bg_image, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                self.backgrounds.extend([scale_bg for _ in range(4)])
            except pygame.error as e:
                print(f"Could not load background image {bg_folder}: {e}")
    
    def spawnMap(self, mapId):
        if mapId < 0 or mapId >= len(self.mapFolders):
            raise IndexError(f"Map ID {mapId} is out of range.")
        
        mapFile = self.mapFolders[mapId]
        size = (30, 100)  # Adjust based on your map size
        
        self.tilemap = Tilemap(self.tileSetFolder, mapFile, size)
        # Initialize the map with all background layers
        self.tilemap.renderMap(self.backgrounds)
    
    def renderMap(self, camera_x=0):
        if self.tilemap:
            self.tilemap.render(self.surface, camera_x)