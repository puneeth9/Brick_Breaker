from common import Common_object
import numpy as np
import os
import colorama 
import time
from colorama import Fore,init,Back
init()
class Display:
    def __init__(self,rows,columns):
        self._rows=rows
        self._columns=columns
        self._grid=self.creategrid(rows,columns)           
    def creategrid(self,rows,columns):
        temp = [[Fore.WHITE + ' ' for x in range(columns)] for y in range(rows-4)]
        return temp 
    def printgrid(self):
        for row in self._grid:
            print("".join(row))
    def object_render(self,object):
        x=round(object.getx())
        y=round(object.gety())
        input=object.getshape()
        a=x
        b=y
        while a >= x and a < x+object.getheight():
            b=y
            while b >= y and b < y+object.getwidth():
                self._grid[a][b]=input[a-x][b-y]
                b=b+1
            a=a+1
    def refreshgrid(self,rows,columns):
        self._grid=self.creategrid(rows,columns)
    def render(self,lives,score,begin):
        #os.system('clear')
        dur=int(time.time() - begin)
        dur=round(dur,2)
        print("\033[0;0H", end='')
        print("Lives: " + str(lives),end="\t")
        print("Score: " + str(score),end="\t")
        print("Time: " + str(dur),end="\n")
        #print(Back.BLUE + (" " * self._columns) + Back.RESET)
        self.printgrid()
        print(Back.BLUE + (" " * self._columns) + Back.RESET)