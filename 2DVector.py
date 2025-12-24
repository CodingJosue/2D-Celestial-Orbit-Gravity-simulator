import math
import  Position

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = math.sqrt(x*x + y*y)

    # use this whenever you want a second type of constructor cls is essential keyword
    @classmethod
    def from_positions(cls, start : Position, end : Position):
        dx = end.x - start.x
        dy = end.y - start.y
        return cls(dx, dy)

