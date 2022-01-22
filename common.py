import time
class Common_object:
    def __init__(self,rows,columns,x,y,height,width,vx,vy):
        self._rows=rows
        self._columns=columns
        self._x=x
        self._y=y
        self._height=height
        self._width=width
        self._vx=vx
        self._vy=vy
        self._active = True
    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def getheight(self):
        return self._height
    def getwidth(self):
        return self._width
    def getvx(self):
        return self._vx
    def getvy(self):
        return self._vy
    def setx(self,x):
        self._x = x
    def sety(self,y):
        self._y = y
    def setheight(self,height):
        self._height = height
    def setwidth(self,width):
        self._width = width
    def incwidth(self,inc):
        self._width = self._width + inc
    def setvx(self,vx):
        self._vx = vx
    def setvy(self,vy):
        self._vy = vy
class Powerup(Common_object):
    def __init__(self,rows,columns,x,y,begin):
        super().__init__(rows,columns,x,y,1,1,1,0)
        self._shape=[None for x in range(self.getheight())]
        self._isactive = False
        self._begin = begin
        self._resetdone=False
        self._ax = 0.5
    def getresetdone(self):
        return self._resetdone
    def set_begin(self,begin):
        self._begin = begin
    def getbegin(self):
        return self._begin
    def check_status(self):
        if(round(int(time.time()-self._begin),2) >=10):
            return True
        else:
            return False
    def getshape(self):
        return self._shape
    def movepowerup(self):
        self._vx = self._vx + self._ax
        if self._y + self._vy <= 0 or self._y +self._vy >= self._columns:
            self._vy = -(self._vy)
        if self._x <= 0:
            self._vx = -(self._vx)
        if self._x <=(self._rows)-5:
            self._x = self._x + self._vx
            self._y = self._y + self._vy
        print("x-coord = " + str(self._x) + " y-coord " + str(self._y),file=open("temp.txt","a"))
    def paddlecollision(self,paddle,brick):
        if self._x <= paddle.getx() and paddle.getx() <= self._x + self._vx + self._ax and self._y in range(paddle.gety(),paddle.gety()+paddle.getwidth()):
            brick.setreceived()
            
            self._isactive = True
            return True
        else:
            return False