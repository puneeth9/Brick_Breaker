from common import Common_object
import numpy as np
from colorama import Fore,Back,Style,init
import random
import colorama
from colorama import Fore , init
import time
init()
class Ball(Common_object):
    def __init__(self,rows,columns,paddlewidth,is_released,start_time):
        self._paddlewidth = paddlewidth
        self._is_released = is_released
        #y=random.randrange(0,self._paddlewidth)
        y=(paddlewidth-1)/2
        vy=y-(paddlewidth-1)/2
        self._start = y
        super().__init__(rows,columns,rows-8,y,1,1,-1,vy)
        self._shape = [[Fore.YELLOW + 'o' for x in range(self.getwidth())] for x in range(self.getheight())]
        self._score=0
        self._isthru = False
        self._start_time = start_time
    def reset(self,rows,columns,paddlewidth,is_released):
        self.setx(rows-8)
        y=(paddlewidth-1)/2
        vy=y-(paddlewidth-1)/2
        self.sety(y)
        self.setheight(1)
        self.setwidth(1)
        self.setvx(-1)
        self.setvy(vy)
        self._is_released = is_released
        self._isthru = False
        self._start = y
        self._start_time = time.time()
    def get_isthru(self):
        return self._isthru
    def set_isthru(self):
        self._isthru = not (self._isthru)
    def getscore(self):
        return self._score
    def setscore(self,final):
        self._score = final
    def incscore(self,inc):
        self._score = self._score + inc 
    def getshape(self):
        return self._shape
    def moveleft_notreleased(self,padvy):
        if self._y > self._start :
            self._y = self._y - padvy
    def moveright_notreleased(self,padvy):
        if self._y + self._paddlewidth - self._start + 1<= self._columns:
            self._y = self._y + padvy
    def set_state(self,is_released):
        self._is_released = is_released
    def start_motion(self):
        if self._y + self._vy <= 0 or self._y +self._vy >= self._columns:
            self._vy = -(self._vy)
        if self._x <= 0:
            self._vx = -(self._vx)
        self._x = self._x + self._vx
        self._y = self._y + self._vy
    def paddle_collision(self,paddle):
        if paddle.getx() == self._x and (self._y - paddle.gety()) in range(0,paddle.getwidth()) :
            self._vx = -(self._vx)
            self._vy = self._vy + (self._y - paddle.gety()) - (paddle.getwidth() -1)/2  
            if paddle.getgrab()==True:
                paddle.setreleased(False)
            if(round(int(time.time()-self._start_time),2) >=30):
                return True  
