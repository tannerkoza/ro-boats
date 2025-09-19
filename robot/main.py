from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu

mission = hub_menu("1", "2", "3", "4")

if mission == "1":
    from mission1 import main
    main()
elif mission == "2":
    from mission2 import main
    main()
elif mission == "3":
    import drop
elif mission == "4":
    import lift


