class Pit:
    def __init__(self, start_x, start_y, end_x, end_y, rows=3, cols=3):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.rows = rows
        self.cols = cols
        self.centers = self._calculate_centers()

    def _calculate_centers(self):
        centers = []
        for row in range(self.rows):
            for col in range(self.cols):
                x = self.start_x + col * (self.end_x - self.start_x) // (self.cols - 1)
                y = self.start_y + row * (self.end_y - self.start_y) // (self.rows - 1)
                centers.append((x, y))
        return centers