from common import Common_object
import numpy as np
import os
import colorama
from colorama import Fore,Back,init
import random
init(autoreset=True)
rows=os.get_terminal_size().lines
columns=os.get_terminal_size().columns
powerups_arr = ['E','S','F','T','G']
class Brick(Common_object):
    def __init__(self,rows,columns,x,y,powerup):
        super().__init__(rows,columns,x,y,2,9,0,0)
        self._status = True
        self._powerup=powerup
        self._powerup_released = False
        self._powerup_received = False
        self._strength = 1
        self._shape = [[None for x in range(self.getwidth())] for x in range(self.getheight())]
    def setreceived(self):
        self._powerup_received = True
    def setreleased(self):
        self._powerup_released = True
    def getreceived(self):
        return self._powerup_received
    def getreleased(self):
        return self._powerup_released
    def getstatus(self):
        return self._status
    def getpowerup(self):
        return self._powerup
    def left_collision(self,ball):
        if (ball.getx() == self._x + self._height - 1 and ball.gety() == self._y and ball.getvy() > 0) or (ball.getx() == self._x and ball.gety() == self._y and ball.getvy() > 0)  :
            return True
        else:
            return False
    def right_collision(self,ball):
        if (ball.getx() == self._x + self._height - 1 and ball.gety() == self._y + self._width - 1 and ball.getvy() < 0) or (ball.getx() == self._x and ball.gety() == self._y + self._width - 1 and ball.getvy() < 0):
            return True
        else:
            return False
    def top_collision(self,ball):
        if ball.getx() == self._x and ball.gety() in range(self._y , self._y + self._width) and ball.getvx() > 0:
            return True
        else:
            return False
    def bottom_collision(self,ball):
        if (ball.getx() == self._x + self._height - 1 and ball.gety() in range(self._y + 1, self._y + self._width-1) and ball.getvx() < 0) or (ball.getx() == self._x + self._height - 1 and (ball.gety()==self._y or ball.gety()==self._y+self._width-1)and ball.getvx()<0 and ball.getvy()==0):
            return True
        else:
            return False
class Break(Brick):
    def __init__(self,rows,columns,x,y,strength,powerup):
        super().__init__(rows,columns,x,y,powerup)
        self._strength = strength
    def getshape(self): 
        for x in range(self.getheight()):
            for y in range(self.getwidth()):
                if x==0 and (y==0 or y==8):
                    self._shape[x][y] = Fore.WHITE + ' '
                elif x==1 and (y==0 or y==8):
                    self._shape[x][y] = Fore.WHITE + '|'
                elif x==0 and y in range(1,8):
                    self._shape[x][y] = Fore.WHITE + '_'
                elif x==1 and y in range(1,8):
                    if self._strength >=5 :
                        self._shape[x][y] = Fore.WHITE + Back.BLUE + '_' + Back.RESET
                    elif self._strength == 4 :
                        self._shape[x][y] = Fore.WHITE + Back.GREEN + '_' + Back.RESET
                    elif self._strength == 3 :
                        self._shape[x][y] = Fore.WHITE + Back.YELLOW + '_' + Back.RESET
                    elif self._strength == 2 :
                        self._shape[x][y] = Fore.WHITE + Back.RED + '_' + Back.RESET
                    elif self._strength == 1 :
                        self._shape[x][y] = Fore.WHITE + Back.BLACK + '_' + Back.RESET
        return self._shape
    def collision(self,ball):
        if (self.left_collision(ball) or self.right_collision(ball)) and self._status == True:
            if ball.get_isthru() == True:
                ball.incscore(self._strength)
                self._strength = 0
            if ball.get_isthru() == False:
                ball.setvy(-ball.getvy())
                self._strength = self._strength - 1
                ball.incscore(1)
            if self._strength == 0:
                os.system("aplay music/brick_break.mp3 -q &")
                self._status = False
                self.setreleased()
                return [ball.getvx(),-ball.getvy()]  
        elif (self.top_collision(ball) or self.bottom_collision(ball)) and self._status == True:
            if ball.get_isthru() == True:
                ball.incscore(self._strength)
                self._strength = 0
            if ball.get_isthru() == False:
                ball.setvx(-ball.getvx())
                self._strength = self._strength - 1
                ball.incscore(1)
            if self._strength == 0:
                os.system("aplay music/brick_break.mp3 -q &")
                self._status = False
                self.setreleased()
                return [-ball.getvx(),ball.getvy()] 
class Unbreak(Brick):
    def __init__(self,rows,columns,x,y,powerup):
        super().__init__(rows,columns,x,y,powerup)
    def getshape(self):
        for x in range(self.getheight()):
            for y in range(self.getwidth()):
                if x==0 and (y==0 or y==8):
                    self._shape[x][y] = Fore.WHITE + ' '
                elif x==1 and (y==0 or y==8):
                    self._shape[x][y] = Fore.WHITE + '|'
                elif x==0 and y in range(1,8):
                    self._shape[x][y] = Fore.WHITE + '_'
                elif x==1 and y in range(1,8):
                    self._shape[x][y] = Fore.WHITE + Back.WHITE + '_' + Back.RESET
        return self._shape

    def collision(self,ball):
        if (self.left_collision(ball) or self.right_collision(ball)) and self._status == True:
            if ball.get_isthru() == True:
                self._status = False
                os.system("aplay music/brick_break.mp3 -q &")
            if ball.get_isthru() == False:
                ball.setvy(-ball.getvy())
        elif (self.top_collision(ball) or self.bottom_collision(ball)) and self._status == True:
            if ball.get_isthru() == True:
                os.system("aplay music/brick_break.mp3 -q &")
                self._status = False
            if ball.get_isthru() == False:
                ball.setvx(-ball.getvx())
class Rainbow_brick(Brick):
    def __init__(self,rows,columns,x,y,strength,powerup):
        super().__init__(rows,columns,x,y,powerup)
        self._blink = True
        self._strength = strength
    def setstrength(self):
        if self._strength in range(1,6):
            self._strength = self._strength + 1
        elif self._strength == 6:
            self._strength = 1
    def getblink(self):
        return self._blink
    def getshape(self): 
        for x in range(self.getheight()):
            for y in range(self.getwidth()):
                if x==0 and (y==0 or y==8):
                    self._shape[x][y] = Fore.WHITE + ' '
                elif x==1 and (y==0 or y==8):
                    self._shape[x][y] = Fore.WHITE + '|'
                elif x==0 and y in range(1,8):
                    self._shape[x][y] = Fore.WHITE + '_'
                elif x==1 and y in range(1,8):
                    if self._strength >=5 :
                        self._shape[x][y] = Fore.WHITE + Back.BLUE + '_' + Back.RESET
                    elif self._strength == 4 :
                        self._shape[x][y] = Fore.WHITE + Back.GREEN + '_' + Back.RESET
                    elif self._strength == 3 :
                        self._shape[x][y] = Fore.WHITE + Back.YELLOW + '_' + Back.RESET
                    elif self._strength == 2 :
                        self._shape[x][y] = Fore.WHITE + Back.RED + '_' + Back.RESET
                    elif self._strength == 1 :
                        self._shape[x][y] = Fore.WHITE + Back.BLACK + '_' + Back.RESET
        return self._shape
    def collision(self,ball):
        if (self.left_collision(ball) or self.right_collision(ball)) and self._status == True:
            self._blink = False
            if ball.get_isthru() == True:
                ball.incscore(self._strength)
                self._strength = 0
            if ball.get_isthru() == False:
                ball.setvy(-ball.getvy())
                self._strength = self._strength - 1
                ball.incscore(1)
            if self._strength == 0:
                os.system("aplay music/brick_break.mp3 -q &")
                self._status = False
                self.setreleased()
                return [ball.getvx(),-ball.getvy()]  
        elif (self.top_collision(ball) or self.bottom_collision(ball)) and self._status == True:
            self._blink = False
            if ball.get_isthru() == True:
                ball.incscore(self._strength)
                self._strength = 0
            if ball.get_isthru() == False:
                ball.setvx(-ball.getvx())
                self._strength = self._strength - 1
                ball.incscore(1)
            if self._strength == 0:
                os.system("aplay music/brick_break.mp3 -q &")
                self._status = False
                self.setreleased()
                return [-ball.getvx(),ball.getvy()] 

Breakable1 = []
Unbreakable1 = []
Rainbow1 = []
temp=0
while temp+9<columns:
    choose = random.randrange(0,3)
    if choose == 0:
        Breakable1.append(Break(rows,columns,round(rows/3),temp,random.randrange(1,6),random.choice(powerups_arr)))
    if choose == 1:
        Unbreakable1.append(Unbreak(rows,columns,round(rows/3),temp,''))
    if choose == 2:
        Rainbow1.append(Rainbow_brick(rows,columns,round(rows/3),temp,random.randrange(1,6),random.choice(powerups_arr)))
    temp = temp+15
count = 0
temp = 3
while temp+9<columns:
    if count%7==0:
        Breakable1.append(Break(rows,columns,round(rows/3)-6,temp,random.randrange(1,6),'E'))
    if count%7==1:
        Breakable1.append(Break(rows,columns,round(rows/3)-6,temp,random.randrange(1,6),'S'))
    if count%7==2:
        Breakable1.append(Break(rows,columns,round(rows/3)-6,temp,random.randrange(1,6),''))
    if count%7==3:
        Rainbow1.append(Rainbow_brick(rows,columns,round(rows/3)-6,temp,random.randrange(1,6),'F'))
    if count%7==4:
        Breakable1.append(Break(rows,columns,round(rows/3)-6,temp,random.randrange(1,6),'T'))
    if count%7==5:
        Breakable1.append(Break(rows,columns,round(rows/3)-6,temp,random.randrange(1,6),''))
    if count%7==6:
        Rainbow1.append(Rainbow_brick(rows,columns,round(rows/3)-6,temp,random.randrange(1,6),'G'))
    count = count + 1
    temp = temp+15  
Breakable2 = []
Unbreakable2 = []
Rainbow2 = []
temp=0
while temp+9<columns:
    Breakable2.append(Break(rows,columns,round(rows/3),temp,random.randrange(1,6),'E'))
    temp = temp+12
temp=3
while temp+9<columns:
    choose = random.randrange(0,3)
    if choose==0:
        Unbreakable2.append(Unbreak(rows,columns,round(rows/3)+5,temp,''))
    elif choose==1:
        Rainbow2.append(Rainbow_brick(rows,columns,round(rows/3)+5,temp,random.randrange(1,6),random.choice(powerups_arr)))
    else:
        Breakable2.append(Break(rows,columns,round(rows/3)+5,temp,random.randrange(1,6),random.choice(powerups_arr)))
    temp = temp+12 
temp=6
while temp+9<columns:
    Breakable2.append(Break(rows,columns,round(rows/3)-10,temp,random.randrange(1,6),random.choice(powerups_arr)))
    temp = temp+12
temp=3
while temp+9<columns:
    choose = random.randrange(0,3)
    if choose==0:
        Unbreakable2.append(Unbreak(rows,columns,round(rows/3)-5,temp,''))
    elif choose==1:
        Breakable2.append(Break(rows,columns,round(rows/3)-5,temp,random.randrange(1,6),random.choice(powerups_arr)))
    else:
        Rainbow2.append(Rainbow_brick(rows,columns,round(rows/3)-5,temp,random.randrange(1,6),random.choice(powerups_arr)))
    temp = temp+12 
temp=6
count = 0 
while temp+9<columns:
    if count%7==0:
        Breakable2.append(Break(rows,columns,round(rows/3)+10,temp,random.randrange(1,6),'E'))
    if count%7==1:
        Breakable2.append(Break(rows,columns,round(rows/3)+10,temp,random.randrange(1,6),'S'))
    if count%7==2:
        Breakable2.append(Break(rows,columns,round(rows/3)+10,temp,random.randrange(1,6),''))
    if count%7==3:
        Rainbow2.append(Rainbow_brick(rows,columns,round(rows/3)+10,temp,random.randrange(1,6),'F'))
    if count%7==4:
        Breakable2.append(Break(rows,columns,round(rows/3)+10,temp,random.randrange(1,6),'T'))
    if count%7==5:
        Breakable2.append(Break(rows,columns,round(rows/3)+10,temp,random.randrange(1,6),''))
    if count%7==6:
        Rainbow2.append(Rainbow_brick(rows,columns,round(rows/3)+10,temp,random.randrange(1,6),'G'))
    count = count + 1
    temp = temp+12  
temp = 0