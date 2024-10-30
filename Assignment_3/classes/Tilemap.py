import pygame, csv, os
import numpy as np
from classes.Tileset import Tileset

class Tilemap:
    def __init__(self, tileSetFile, mapFile, size=(30, 20), screenSize = (800, 600), rect=None):
        self.size = size
        self.tileSetFile = tileSetFile
        self.map = self.read_csv(mapFile)
        self.tileset = Tileset(tileSetFile)
        
        #
        h, w = self.size
        self.image = pygame.Surface(screenSize)
        if rect:
            self.rect = pygame.Rect(rect)
        else:   
            self.rect = self.image.get_rect()



    def renderMap(self, background):
        self.drawBackground(background)
        m, n = self.map.shape
        for i in range(m):
            for j in range(n):
                if self.map[i][j] != -1:
                    tile = self.tileset.tiles[self.map[i][j]]
                    self.image.blit(tile, (j*32, i*32))


    def read_csv(self, fileName):
        map_data = []
        with open(os.path.join(fileName)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map_data.append(list(map(int, row)))
        return np.array(map_data)

    def drawBackground(self, background):
        if background:
            self.image.blit(background, (0, 0))

    def render(self, surface: pygame.Surface):
        dest = (0, 0)
        #area = pygame.Rect(0, 0, 400, 600)
        surface.blit(self.image, dest)


    def __str__(self):
        return f'{self.__class__.__name__} {self.size}'      