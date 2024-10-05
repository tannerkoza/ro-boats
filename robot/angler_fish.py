from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

def inches_to_mm(inches):
    return inches * 25.4

wheel_diameter = inches_to_mm(inches=3.375)
axle_track = inches_to_mm(inches=5.875)

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
Bucket_Motor = Motor(Port.D)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=axle_track)

# Optionally, uncomment the line below to use the gyro for improved accuracy.
drive_base.use_gyro(True)

# Drive forward by 500mm (half a meter).

# Turn around clockwise by 180 degrees.
drive_base.turn(-90)

drive_base.straight(inches_to_mm(inches=4.5))
drive_base.turn(90)

drive_base.straight(inches_to_mm(inches=7.5))




# Drive forward again to get back to the start.
# drive_base.straight(500)

# Turn around counterclockwise.
# drive_base.turn(-180)
