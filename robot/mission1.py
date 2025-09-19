from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

def main():
    drive_base = initialize()
    mission(drive_base=drive_base)

def mission(drive_base):
    # drive to ship
    drive_base.straight((inches_to_mm(12)))

    wait(sec_to_msec(2))

    # drive backwards from ship
    drive_base.straight((inches_to_mm(-8)))

    # turn left 90
    drive_base.turn(-90)

    # drive out from edge
    drive_base.straight((inches_to_mm(6)))

    # turn right 90
    drive_base.turn(90)

    # drive to lift ship
    drive_base.straight((inches_to_mm(16)))

    # back away from ship to return to blue
    drive_base.straight((inches_to_mm(-5.5)))

    # turn left 45
    drive_base.turn(-45)

    drive_base.straight((inches_to_mm(8)))

    drive_base.turn(45)

    drive_base.straight((inches_to_mm(10)))

    drive_base.turn(20)

    drive_base.straight((inches_to_mm(30)))
def initialize():
    # initialization
    LEFT_MOTOR = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    RIGHT_MOTOR = Motor(Port.E)

    WHEEL_DIAMETER = inches_to_mm(inches=3.375)
    AXLE_TRACK = inches_to_mm(inches=5.875)
    MOTOR_SPEED = 360 # [deg/s]
    DUTY_LIMIT = 75 # %
    TURN_RATE = 45 # [deg/s]

    drive_base = DriveBase(left_motor=LEFT_MOTOR, right_motor=RIGHT_MOTOR, wheel_diameter=WHEEL_DIAMETER, axle_track=AXLE_TRACK)
    drive_base.use_gyro(True)
    drive_base.settings(turn_rate=TURN_RATE)

    return drive_base


def inches_to_mm(inches):
    return inches * 25.4

def sec_to_msec(sec):
    return sec * 1000

if __name__ == "__main__":
    main()