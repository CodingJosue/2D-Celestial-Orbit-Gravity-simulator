from Body import Body
class Star(Body):
    def __init__(self, name, px, py, mass, radius, color):
        super().__init__(name, px, py, mass, radius, color)
        self.isHeavy = True
