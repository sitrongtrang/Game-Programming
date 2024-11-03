import pygame, csv, os
import numpy as np
from classes.Tileset import Tileset

class Tilemap:
    def __init__(self, tileSetFile, mapFile, size=(10, 20), rect=None):
        self.size = size
        self.tileSetFile = tileSetFile
        self.map = self.read_csv(mapFile)
        self.tileset = Tileset(tileSetFile, size)

        h, w = self.size
        self.image = pygame.Surface((32*w, 32*h))
        if rect:
            self.rect = pygame.Rect(rect)
        else:
            self.rect = self.image.get_rect()


    def renderMap(self):
        m, n = self.map.shape
        for i in range(m):
            for j in range(n):
                tile = self.tileset.tiles[self.map[i, j]]
                self.image.blit(tile, (j*32, i*32))

    def read_csv(self, fileName):
        map_data = []
        with open(os.path.join(fileName)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map_data.append(list(map(int, row)))
        return map_data




    def __str__(self):
        return f'{self.__class__.__name__} {self.size}'      