import pygame, csv, os
import numpy as np
from classes.Tileset import Tileset
from data import constant

class Tilemap:
    def __init__(self, tileSetFile, mapFile, size=(10, 20), rect=None):
        self.size = size
        if tileSetFile != "":
            self.tileSetFile = tileSetFile
            self.tileset = Tileset(tileSetFile, size)
        self.map = np.array(self.read_csv(mapFile))
        self.player_position = None
        self.boss_position = None
        self.enemy_positions = []
        self.platform_positions = []
        self.item_positions = []
        self.coin_positions = []

        h, w = self.size
        self.image = pygame.Surface((constant.TILE_SIZE * w, constant.TILE_SIZE * h))
        if rect:
            self.rect = pygame.Rect(rect)
        else:
            self.rect = self.image.get_rect()


    def renderMap(self):
        m, n = self.map.shape
        for i in range(m):
            for j in range(n):
                tile_value = self.map[i, j]
                if tile_value == 0:
                    continue  # Empty space, no tile rendered
                elif tile_value == 1:
                    # Platform tile
                    self.platform_positions.append((j * constant.TILE_SIZE, i * constant.TILE_SIZE))
                elif tile_value == 2:
                    # Player starting position
                    self.player_position = (j * constant.TILE_SIZE, i * constant.TILE_SIZE)
                elif tile_value == 3:
                    # Enemy spawn point
                    self.enemy_positions.append((j * constant.TILE_SIZE, i * constant.TILE_SIZE))
                elif tile_value == 4:
                    # Item spawn point
                    self.item_positions.append((j * constant.TILE_SIZE, i * constant.TILE_SIZE))
                elif tile_value == 5:
                    # Coin spawn point
                    self.coin_positions.append((j * constant.TILE_SIZE, i * constant.TILE_SIZE))
                elif tile_value == 6:
                    # Boss spawn point
                    self.boss_position = (j * constant.TILE_SIZE, i * constant.TILE_SIZE)

                # tile = self.tileset.tiles[self.map[i, j]]
                # self.image.blit(tile, (j*constant.TILE_SIZE, i*constant.TILE_SIZE))

    def read_csv(self, fileName):
        map_data = []
        with open(os.path.join(fileName)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map_data.append(list(map(int, row)))
        return map_data




    def __str__(self):
        return f'{self.__class__.__name__} {self.size}'      