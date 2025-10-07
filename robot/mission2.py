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
    drive_base.straight(inches_to_mm(25))
    drive_base.turn(35)
    drive_base.straight(inches_to_mm(3))
    drive_base.turn(-80)
    drive_base.straight((inches_to_mm(3.5)))
    drive_base.turn(-45)
    wait(sec_to_msec(1))
    drive_base.straight(inches_to_mm(-1.5))
    drive_base.turn(-30)
    drive_base.straight(inches_to_mm(2))
    drive_base.turn(35)
    drive_base.straight(inches_to_mm(10))
    drive_base.turn(45)
    # drive_base.straight(inches_to_mm(-6.5))
    # wait(sec_to_msec(1))
    # drive_base.straight(inches_to_mm(4))
    # drive_base.turn(-35)
    # drive_base.straight(inches_to_mm(-10))
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