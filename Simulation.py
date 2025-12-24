import pygame
import Body
class Simulation:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800,800))
        self.bodies = []
        self.running = True

    def physics(self):
        for body1 in self.bodies:
            for body2 in self.bodies:
                if body1 == body2: continue
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False



