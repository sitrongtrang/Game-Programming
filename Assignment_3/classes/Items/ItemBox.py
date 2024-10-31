class ItemBox:
    def __init__(self, x, y, width, height, item):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.triggered = False
        self.item = item

    def update(self):
        pass