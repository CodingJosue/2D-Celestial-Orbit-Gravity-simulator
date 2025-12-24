import pygame
import Body
from Physics import Physics
from Vector2D import Vector2D
class Simulation:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800,800))
        self.bodies = []
        self.running = True

    def physics(self, dt):
        for body1 in self.bodies:
            body1.force = Vector2D(0,0)
            for body2 in self.bodies:
                if body1.__eq__(body2): continue
                body1.force = body1.force.add(Physics.calculateForce(body1, body2))


        for body in self.bodies:
            body.update(dt)
            #update each individual body
    def run(self):
        dt = 24 * 3600
        while self.running:
            #1. clear the screen âint it black
            self.window.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #4. run the physics
            self.physics(dt)
            for body in self.bodies:
                body.draw(self.window)

            #5 refresh the monitor other wise wil ldraw all the planets at each position
            pygame.display.flip()


