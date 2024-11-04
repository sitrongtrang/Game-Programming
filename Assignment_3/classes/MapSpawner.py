import pygame
from classes.Tilemap import Tilemap
import os

class MapSpawner:
    def __init__(self, surface, mapNumber):
        self.surface = surface
        self.mapNumber = mapNumber

        self.mapFolders = [
            os.path.join("data", "maps", "TestMap.csv")
        ]

        self.tileSetFolder = os.path.join("assets", "maps", "tileset.png")
        self.backgroundFolder = os.path.join("assets", "maps", "Background.png")
        self.tilemap = None

        # Tải ảnh nền
        self.background = self.loadBackground()

    def loadBackground(self):
        try:
            return pygame.image.load(self.backgroundFolder).convert()
        except pygame.error as e:
            print(f"Could not load background image: {e}")
            return None

   

    def spawnMap(self, mapId):
        if mapId < 0 or mapId >= len(self.mapFolders):
            raise IndexError(f"Map ID {mapId} is out of range.")

        mapFile = self.mapFolders[mapId]
        size = (10, 20)

        self.tilemap = Tilemap(self.tileSetFolder, mapFile, size)
        self.tilemap.renderMap(self.background)

    def renderMap(self, camera = None):
        # Vẽ background trước khi render tilemap
        if self.tilemap:
            self.tilemap.render(self.surface)
