#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# initialize components
ev3 = EV3Brick()
right_motor: Motor = Motor(Port.C)
left_motor: Motor = Motor(Port.B)
color_sensor: ColorSensor = ColorSensor(Port.S1)

def turn_left(speed: int):
    left_motor.stop()
    right_motor.run(speed)

def turn_right(speed: int):
    right_motor.stop()
    left_motor.run(speed)

# execution part
while True:
    is_on_line: bool = color_sensor.reflection < 10
    if is_on_line:
        turn_right(30)
        continue
    turn_left(30)