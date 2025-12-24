import pygame
import  Position
import  Vector2D
class Body:
    AU = 1.496e11
    SCALE = 250/ AU
    def __init__(self, name,px, py, mass, radius, color):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.color = color

        self.position = Position(px, py)
        self.velocity = Vector2D(0, 0)
        self.acceleration = Vector2D(0, 0)
        self.force = Vector2D(0, 0)


    def getMass(self): return self.mass
    def getPosition(self): return self.position
    def getVelocity(self): return self.velocity
    def getAcceleration(self): return self.acceleration
    def getForce(self): return self.force

    def draw(self, window):
        px = self.position.x * self.SCALE + (window.get_width() / 2)
        py = self.position.y * self.SCALE + (window.get_height() / 2)
        pygame.draw.circle(window, self.color, (int(px), int(py)), self.radius)

    def update(self, force : Vector2D, dt):
        acceleration = force.scale(1/self.mass) # the new acceleration is based on the sum of all forces no need to sum acceleration
        self.velocity = self.velocity.add(acceleration.scale(dt))
        self.position = self.position.add(acceleration.scale(dt))




