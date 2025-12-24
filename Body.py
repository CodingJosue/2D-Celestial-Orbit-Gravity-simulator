import  Position
import  Vector2D
class Body:
    def __init__(self, px, py, mass, radius, color):
        self.mass = mass
        self.radius = radius
        self.color = color

        self.position = Position(px, py)
        self.velocity = Vector2D(0, 0)
        self.acceleration = Vector2D(0, 0)
        self.force = Vector2D(0, 0)


    def getPosition(self): return self.position
    def getVelocity(self): return self.velocity
    def getAcceleration(self): return self.acceleration
    def getForce(self): return self.force


