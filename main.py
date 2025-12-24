# This is a sample Python script.
from Simulation import Simulation
from Body import  Body
from Vector2D import Vector2D

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def main():
    sim = Simulation()

    # 1. Create the Sun (Center of the world)
    sun = Body("Sun", 0, 0, 1.989e30, 15, (255, 255, 0))

    # 2. Create Earth (1 AU away)
    # Note: We set vy to 29780 m/s to keep it in a stable orbit
    earth = Body("Earth", 1.496e11, 0, 5.972e24, 8, (100, 149, 237))
    earth.velocity = Vector2D(0, 29780)

    # 3. Create Venus (Roughly 0.72 AU away)
    venus = Body("Venus", 1.082e11, 0, 4.867e24, 7, (255, 198, 112))
    venus.velocity = Vector2D(0, 35020)

    # Add them to the simulation list
    sim.bodies = [sun, earth, venus]

    # Start the engine!
    sim.run()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main()
#
#
