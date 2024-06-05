#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Feladatok:

        def __init__(self):
                self.ev3 = EV3Brick()
                self.m = Motor(Port.A)
                
        def le(self):
                self.m.run(-150)

        def ontozes1(self):
                while(True):
                        if self.ev3.buttons.pressed()==[Button.UP]:
                                self.le()
                                wait(500)
                                self.ev3.speaker.play_file("water.wav")


        def csipog(self):
                self.ev3.speaker.beep()