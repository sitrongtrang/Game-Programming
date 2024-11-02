import pygame

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        # Adjust the entity's position based on camera's position
        return entity.rect.move(-self.camera.x, -self.camera.y)

    def update(self, target):
        # Center the camera on the target (player)
        x = target.rect.centerx - self.width // 2
        y = target.rect.centery - self.height // 2

        # Keep the camera within bounds
        x = max(0, min(x, self.width - self.camera.width))
        y = max(0, min(y, self.height - self.camera.height))

        self.camera = pygame.Rect(x, y, self.camera.width, self.camera.height)
