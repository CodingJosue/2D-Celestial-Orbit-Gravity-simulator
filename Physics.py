import math
from Body import  Body
from Vector2D import  Vector2D
class Physics:
    G = 6.67428e-11
    @staticmethod
    def rVector(b1: Body, b2 : Body):
        r = Vector2D(b1.position.x - b2.position.x, b1.position.y - b2.position.y).normalize().scale(-1)

        return r

    @staticmethod
    def calculateForce(b1: Body, b2 : Body):
        # force on b1 by b2
        m1 = b1.getMass()
        m2 = b2.getMass()
        distance =  Vector2D(b1.position.x - b2.position.x, b1.position.y - b2.position.y)
        force =   Physics.rVector(b1, b2).scale(Physics.G * m1 * m2 / pow(distance.calcMagnitude(), 2))
        return force




