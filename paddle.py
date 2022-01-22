from common import Common_object
import numpy as np
import colorama
from colorama import Fore,init
init()
class Paddle(Common_object):
    def __init__(self,rows,columns):
        super().__init__(rows,columns,rows-8,0,1,7,0,2)
        self._shape=[[Fore.YELLOW + '_' for x in range(self.getwidth())] for x in range(self.getheight())] 
        self._is_released=False
        self._grab = True
    def reset(self,rows,columns):
        self._is_released = False
        self._grab = True
        self.setx(rows-8)
        self.sety(0)
        self.setheight(1)
        self.setwidth(7)
        self.setvx(0)
        self.setvy(2)
    def getgrab(self):
        return self._grab
    def setgrab(self,input):
        self._grab = input
    def getreleased(self):
        return self._is_released
    def setreleased(self,input):
        self._is_released = input
    def getshape(self):
        self._shape=[[Fore.YELLOW + '_' for x in range(self.getwidth())] for x in range(self.getheight())]
        return self._shape
    def moveleft(self):
        if not self.leftcollision() :
            self._y=(self._y)-self._vy
    def moveright(self):
        if not self.rightcollision() : 
            self._y=(self._y)+self._vy
    def rightcollision(self):
        if (self._y + self._width >= self._columns) or (self._y + self._width + 1 == self._columns) :
            return True
        else:
            return False
    def leftcollision(self):
        if self._y <= 0 :
            return True
        else:
            return False