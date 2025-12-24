from Body import Body
class Planet(Body):
    def __init__(self, name,px, py, mass, radius, color):
        super().__init__(name, px, py, mass, radius, color)