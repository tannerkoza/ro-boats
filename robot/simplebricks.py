from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Initialize motors on port A and B.
LEFT_WHEEL = Motor(Port.A)
RIGHT_WHEEL = Motor(Port.E)

circumference = 10.6023 # inches

def move_forward(distance):

    LEFT_WHEEL.run(-360)
    RIGHT_WHEEL.run(360)

    time = (distance / circumference) * 1000 # ms
    wait(time)

def move_backward(distance):

    LEFT_WHEEL.run(360)
    RIGHT_WHEEL.run(-360)

    time = (distance / circumference) * 1000 # ms

    wait(time)


def stop():
    LEFT_WHEEL.stop()
    RIGHT_WHEEL.stop()
