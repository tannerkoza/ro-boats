from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from simplebricks import move_forward, move_backward

hub = PrimeHub()


move_forward(14)
wait(3000)
move_backward(15)
# Wait for three seconds.
# wait(4000)
move_forward(32.5)


