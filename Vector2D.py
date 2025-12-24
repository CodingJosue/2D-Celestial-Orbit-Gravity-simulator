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

    #adding a vector creaetes a new vector
    def add(self, otherVector):
        return Vector2D(self.x + otherVector.x, self.y + otherVector.y)

    def calcMagnitude(self):
        self.magnitude = math.sqrt(self.x**2 + self.y**2)
    # scale the current vector
    def scale(self, factor):
       return Vector2D(self.x * factor, self.y * factor)

    def normalize(self):
        if self.magnitude == 0:
            return
        return Vector2D(self.x / self.magnitude, self.y/self.magnitude)

    def setValue(self, x, y):
        self.x = x
        self.y = y
        self.calcMagnitude()

