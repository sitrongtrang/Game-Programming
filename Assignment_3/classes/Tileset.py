import pygame
from data import constant

class Tileset:
    def __init__(self, file, size = (constant.TILE_SIZE, constant.TILE_SIZE), margin = 0, spacing = 0):
        self.file = file
        self.size = size
        self.margin = margin
        self.spacing = spacing
        self.tiles = []

        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()

        self.load()
        
    def load(self):

        self.tiles = []
        x0 = y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing
        
        for x in range(x0, w, dx):
            for y in range(y0, h, dy):
                tile = pygame.Surface(self.size)
                tile.blit(self.image, (0, 0), (x, y, *self.size))
                self.tiles.append(tile)

    

    def __str__(self):
        return f'{self.__class__.__name__} file:{self.file} tile:{self.size}'