import math
import  Body
import  Vector2D
class Physics:
    G = 6.67428e-11
    @staticmethod
    def rVector(b1: Body, b2 : Body):
        r = Vector2D(b1.x - b2.x, b1.y - b2.y)
        r.normalize()
        return r

    @staticmethod
    def calculateForce(b1: Body, b2 : Body):
        # force on b1 by b2
        m1 = b1.getMass()
        m2 = b2.getMass()
        distance =  Vector2D(b1.x - b2.x, b1.y - b2.y)
        force = (Physics.G * m1 * m2 / (distance.calcMagnitude()**2)) * Physics.rVector(b1, b2)
        return force

    @staticmethod
    def calculateAcceleration(b1: Body, b2 : Body):
        acceleration = Physics.calculateForce(b1, b2).scale(1/b1.getMass())
        return acceleration

    @staticmethod
    def calculateVelocity(b1: Body, b2 : Body, dt):
        velocity = Physics.calculateAcceleration(b1, b2).scale(dt)
        return velocity
    @staticmethod
    def calculatePosition(b1: Body, b2 : Body, dt):
        position = Physics.calculateVelocity(b1, b2, dt).scale(dt)
        return position



