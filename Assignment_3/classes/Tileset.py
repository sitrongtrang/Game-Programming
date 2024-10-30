import pygame

class Tileset:
    def __init__(self, file, size=(32, 32), margin=0, spacing=0):
        self.file = file
        self.size = size
        self.margin = margin
        self.spacing = spacing
        self.tiles = []

        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        print(self.rect)
        self.load()
        
    def load(self):
        self.tiles = []
        x0 = y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing
        
        for y in range(y0, h, dy):      # Đổi vị trí vòng lặp x và y
            for x in range(x0, w, dx):
                tile = pygame.Surface(self.size, pygame.SRCALPHA)  # Khởi tạo với độ trong suốt
                tile.blit(self.image, (0, 0), (x, y, *self.size))  # Sửa lỗi thứ tự tọa độ
                self.tiles.append(tile)

    def __str__(self):
        return f'{self.__class__.__name__} file:{self.file} tile:{self.size}'
