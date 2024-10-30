import pygame


class Spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename)
            if not self.sheet.get_alpha():
                self.sheet.set_colorkey((0, 0, 0))
        except pygame.error:
            print("Unable to load spritesheet image:", filename)
            raise SystemExit

    def image_at(
        self,
        x,
        y,
        scalingfactor,
        colorkey=(0, 0, 0),  # Defaulting colorkey to black
        ignoreTileSize=False,
        xTileSize=8 * 6,
        yTileSize=16,
    ):
        if ignoreTileSize:
            rect = pygame.Rect((x, y, xTileSize, yTileSize))
        else:
            rect = pygame.Rect((x * xTileSize, y * yTileSize, xTileSize, yTileSize))

        # Create a new surface with alpha support
        image = pygame.Surface(rect.size, pygame.SRCALPHA)

        # Blit the part of the spritesheet onto the new image
        image.blit(self.sheet, (0, 0), rect)

        # Set the colorkey if provided
        if colorkey is not None:
            image.set_colorkey(colorkey, pygame.RLEACCEL)

        # Scale the image and return
        return pygame.transform.scale(
            image, (xTileSize * scalingfactor, yTileSize * scalingfactor)
        )
