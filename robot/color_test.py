from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from simplebricks import move_forward, move_backward, stop

hub = PrimeHub()
left_color = ColorSensor(Port.B)
right_color = ColorSensor(Port.F)

while True:
    move_forward(5)
    color = left_color.color()
    print(color)

    if color == Color.WHITE:

        break
        stop()