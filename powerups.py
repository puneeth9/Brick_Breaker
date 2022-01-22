from common import Common_object , Powerup
import time
import os
class Expand(Powerup):
    def __init__(self,rows,columns,x,y,begin):
        super().__init__(rows,columns,x,y,begin)
    def getshape(self):
        self._shape = ['E'  for x in range(self.getheight())]
        return self._shape
    def paddlecollision(self,paddle,ball,brick):
        if self._x <= paddle.getx() and paddle.getx() <= self._x + self._vx + self._ax and self._y in range(paddle.gety(),paddle.gety()+paddle.getwidth()) and brick.getreceived() == False:
            brick.setreceived()
            os.system("aplay music/power_up.mp3 -q &")
            paddle.incwidth(2)
            self.set_begin(time.time())
            self._isactive = True
            return True
        else:
            return False
    def reset(self,paddle,ball):
        if self.check_status() == True and self._isactive == True:
            paddle.incwidth(-2)
            self._isactive = False
            self._resetdone = True
class Shrink(Powerup):
    def __init__(self,rows,columns,x,y,begin):
        super().__init__(rows,columns,x,y,begin)
    def getshape(self):
        self._shape = ['S'  for x in range(self.getheight())]
        return self._shape
    def paddlecollision(self,paddle,ball,brick):
        if self._x <= paddle.getx() and paddle.getx() <= self._x + self._vx + self._ax and self._y in range(paddle.gety(),paddle.gety()+paddle.getwidth()) and brick.getreceived() == False:
            brick.setreceived()
            os.system("aplay music/power_up.mp3 -q &")
            if paddle.getwidth() > 3:
                paddle.incwidth(-2)
            self.set_begin(time.time())
            self._isactive = True
            return True
        else:
            return False
    def reset(self,paddle,ball):
        if self.check_status() == True and self._isactive == True:
            print("Reset Done",file=open("temp.txt","a"))
            if paddle.getwidth() > 1:
                paddle.incwidth(2)
            self._isactive = False
            self._resetdone = True
class FastBall(Powerup):
    def __init__(self,rows,columns,x,y,begin):
        super().__init__(rows,columns,x,y,begin)
    def getshape(self):
        self._shape = ['F'  for x in range(self.getheight())]
        return self._shape
    def check_status(self):
        if(round(int(time.time()-self._begin),2) >=20):
            return True
        else:
            return False
    def paddlecollision(self,paddle,ball,brick):
        if self._x <= paddle.getx() and paddle.getx() <= self._x + self._vx + self._ax and self._y in range(paddle.gety(),paddle.gety()+paddle.getwidth()) and brick.getreceived() == False:
            brick.setreceived()
            os.system("aplay music/power_up.mp3 -q &")
            ball.setvx((2)*ball.getvx())
            ball.setvy((2)*ball.getvy())
            self.set_begin(time.time())
            self._isactive = True
            return True
        else:
            return False
    def reset(self,paddle,ball):
        if self.check_status() == True and self._isactive == True:
            print("Reset Done",file=open("temp.txt","a"))
            ball.setvx(ball.getvx()/2)
            ball.setvy(ball.getvy()/2)
            self._isactive = False
            self._resetdone = True
class ThruBall(Powerup):
    def __init__(self,rows,columns,x,y,begin):
        super().__init__(rows,columns,x,y,begin)
    def getshape(self):
        self._shape = ['T'  for x in range(self.getheight())]
        return self._shape
    def check_status(self):
        if(round(int(time.time()-self._begin),2) >=20):
            return True
        else:
            return False
    def paddlecollision(self,paddle,ball,brick):
        if self._x <= paddle.getx() and paddle.getx() <= self._x + self._vx + self._ax and self._y in range(paddle.gety(),paddle.gety()+paddle.getwidth()) and brick.getreceived() == False:
            brick.setreceived()
            os.system("aplay music/power_up.mp3 -q &")
            ball.set_isthru()
            self.set_begin(time.time())
            self._isactive = True
            return True
        else:
            return False
    def reset(self,paddle,ball):
        if self.check_status() == True and self._isactive == True:
            print("Reset Done",file=open("temp.txt","a"))
            ball.set_isthru()
            self._isactive = False
            self._resetdone = True
class GrabBall(Powerup):
    def __init__(self,rows,columns,x,y,begin):
        super().__init__(rows,columns,x,y,begin)
    def getshape(self):
        self._shape = ['G'  for x in range(self.getheight())]
        return self._shape
    def check_status(self):
        if(round(int(time.time()-self._begin),2) >= 20):
            return True
        else:
            return False
    def paddlecollision(self,paddle,ball,brick):
        if self._x <= paddle.getx() and paddle.getx() <= self._x + self._vx + self._ax and self._y in range(paddle.gety(),paddle.gety()+paddle.getwidth()) and brick.getreceived() == False:
            brick.setreceived()
            os.system("aplay music/power_up.mp3 -q &")
            paddle.setgrab(True)
            ball.setvx(-ball.getvx())
            self.set_begin(time.time())
            self._isactive = True
            return True
        else:
            return False
    def reset(self,paddle,ball):
        if self.check_status() == True and self._isactive == True:
            paddle.setgrab(False)
            self._isactive = False
            self._resetdone = True