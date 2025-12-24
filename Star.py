import Body
class Star(Body):
    def __init__(self, px, py, mass, radius, color):
        super().__init__(px, py, mass, radius, color)
        self.isHeavy = True
