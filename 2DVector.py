import math


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = math.sqrt(x*x + y*y)

    @classmethod
    def from_positions(cls, start, end):
        dx = end.x - start.x
        dy = end.y - start.y
        return cls(dx, dy)

