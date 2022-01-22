import sys
import termios
import tty
import signal
import input
import os
import time
import numpy as np
from display import Display
from common import Common_object,Powerup
from powerups import *
from paddle import Paddle
from ball import Ball
from brick import Brick,Break,Unbreak,Rainbow_brick,Breakable1,Unbreakable1,Rainbow1,Breakable2,Unbreakable2,Rainbow2
import colorama
colorama.init(autoreset=True)
os.system('clear')
rows=os.get_terminal_size().lines
columns=os.get_terminal_size().columns
display=Display(rows,columns)
lives = 3
life_score=[]
powerup_list1=[]
for brick in Breakable1:
    if brick.getpowerup() == '':
        powerup_list1.append(None)
    elif brick.getpowerup() == 'E':
        powerup_list1.append(Expand(rows,columns,brick.getx(),brick.gety(),0))
    elif brick.getpowerup() == 'S':
        powerup_list1.append(Shrink(rows,columns,brick.getx(),brick.gety(),0))
    elif brick.getpowerup() == 'F':
        powerup_list1.append(FastBall(rows,columns,brick.getx(),brick.gety(),0))
    elif brick.getpowerup() == 'T':
        powerup_list1.append(ThruBall(rows,columns,brick.getx(),brick.gety(),0))
    elif brick.getpowerup() == 'G':
        powerup_list1.append(GrabBall(rows,columns,brick.getx(),brick.gety(),0))
for brick in Rainbow1:
    if brick.getpowerup() == '':
        powerup_list1.append(None)
    elif brick.getpowerup() == 'E':
        powerup_list1.append(Expand(rows,columns,brick.getx(),brick.gety(),0))
    elif brick.getpowerup() == 'S':
        powerup_list1.append(Shrink(rows,columns,brick.getx(),brick.gety(),0))
    elif brick.getpowerup() == 'F':
        powerup_list1.append(FastBall(rows,columns,brick.getx(),brick.gety(),0))
    elif brick.getpowerup() == 'T':
        powerup_list1.append(ThruBall(rows,columns,brick.getx(),brick.gety(),0))
    elif brick.getpowerup() == 'G':
        powerup_list1.append(GrabBall(rows,columns,brick.getx(),brick.gety(),0))
powerup_list2=[]
for brick in Breakable2:
    if brick.getpowerup() == '':
        powerup_list2.append(None)
    elif brick.getpowerup() == 'E':
        powerup_list2.append(Expand(rows,columns,brick.getx(),brick.gety(),0))
    elif brick.getpowerup() == 'S':
        powerup_list2.append(Shrink(rows,columns,brick.getx(),brick.gety(),0))
    elif brick.getpowerup() == 'F':
        powerup_list2.append(FastBall(rows,columns,brick.getx(),brick.gety(),0))
    elif brick.getpowerup() == 'T':
        powerup_list2.append(ThruBall(rows,columns,brick.getx(),brick.gety(),0))
    elif brick.getpowerup() == 'G':
        powerup_list2.append(GrabBall(rows,columns,brick.getx(),brick.gety(),0))
for brick in Rainbow2:
    if brick.getpowerup() == '':
        powerup_list2.append(None)
    elif brick.getpowerup() == 'E':
        powerup_list2.append(Expand(rows,columns,brick.getx(),brick.gety(),0))
    elif brick.getpowerup() == 'S':
        powerup_list2.append(Shrink(rows,columns,brick.getx(),brick.gety(),0))
    elif brick.getpowerup() == 'F':
        powerup_list2.append(FastBall(rows,columns,brick.getx(),brick.gety(),0))
    elif brick.getpowerup() == 'T':
        powerup_list2.append(ThruBall(rows,columns,brick.getx(),brick.gety(),0))
    elif brick.getpowerup() == 'G':
        powerup_list2.append(GrabBall(rows,columns,brick.getx(),brick.gety(),0))
def total_score(arr):
    total=0
    for ele in arr:
        total = total + ele
    return total
begin=time.time()
paddle=Paddle(rows,columns)
ball = Ball(rows,columns,paddle.getwidth(),paddle.getreleased(),time.time())
level = 1
level_finished = False
Breakable = Breakable1
Unbreakable = Unbreakable1
Rainbow = Rainbow1
powerup_list = powerup_list1
while lives > 0:
    paddle.reset(rows,columns)
    ball.reset(rows,columns,paddle.getwidth(),paddle.getreleased())
    release_frame=0
    while True:
        display.refreshgrid(rows,columns)
        if level == 3:
            sys.exit("Game Over")
        if level_finished == True:
            paddle.reset(rows,columns)
            ball.reset(rows,columns,paddle.getwidth(),paddle.getreleased())
            release_frame=0
            level_finished = False
            if level == 2:
                Breakable = Breakable2
                Unbreakable = Unbreakable2
                Rainbow = Rainbow2
                powerup_list = powerup_list2
        temp=0
        for brick in Breakable:
            if brick.getstatus() == True:
                powerup_vel = brick.collision(ball)
                if powerup_list[temp] != None and powerup_vel!=None:
                    powerup_list[temp].setvx(powerup_vel[0])
                    powerup_list[temp].setvy(powerup_vel[1])
            if powerup_list[temp] != None:
                if brick.getstatus() == False and brick.getreleased() == False:
                    brick.setreleased()
                if brick.getreleased() == True and brick.getreceived() == False:
                    powerup_list[temp].movepowerup()
                    powerup_list[temp].paddlecollision(paddle,ball,brick)
                if powerup_list[temp].getresetdone() == False and brick.getreceived()==True:
                    powerup_list[temp].reset(paddle,ball)
            temp = temp + 1
                     
        for brick in Unbreakable:
            brick.collision(ball) 
        for brick in Rainbow:
            if brick.getblink() == True:
                brick.setstrength()
            if brick.getstatus() == True:
                powerup_vel = brick.collision(ball)
                if powerup_list[temp] != None and powerup_vel!=None:
                    powerup_list[temp].setvx(powerup_vel[0])
                    powerup_list[temp].setvy(powerup_vel[1])
            if powerup_list[temp] != None:
                if brick.getstatus() == False and brick.getreleased() == False:
                    brick.setreleased()
                if brick.getreleased() == True and brick.getreceived() == False:
                    powerup_list[temp].movepowerup()
                    powerup_list[temp].paddlecollision(paddle,ball,brick)
                if powerup_list[temp].getresetdone() == False and brick.getreceived()==True:
                    powerup_list[temp].reset(paddle,ball)
            temp = temp + 1
        press=input.input_to(input.Get())
        if press =="q" or ball.getx() > paddle.getx():
            break
        if press == "l":
            level = level+1
            level_finished = True
            continue
        if press == "a":
            paddle.moveleft()
            if paddle.getreleased()==False:
                ball.moveleft_notreleased(paddle.getvy())
        if press == "d":
            if paddle.getreleased()==False and not paddle.rightcollision():
                ball.moveright_notreleased(paddle.getvy())
            paddle.moveright()
        if press == " ":
            paddle.setgrab(False)
            paddle.setreleased(not(paddle.getreleased()))
            ball.set_state(paddle.getreleased())
        if paddle.getreleased() == 1:
            release_frame = release_frame+1
            if release_frame > 1:
                falling_bricks = ball.paddle_collision(paddle)
                if falling_bricks == True:
                    for brick in Breakable:
                        if brick.getx()+1 == paddle.getx():
                            sys.exit("Game Over")
                        brick.setx(brick.getx()+1)
                    for brick in Unbreakable:
                        if brick.getx()+1 == paddle.getx():
                            sys.exit("Game Over")
                        brick.setx(brick.getx()+1)
                    for brick in Rainbow:
                        if brick.getx()+1 == paddle.getx():
                            sys.exit("Game Over")
                        brick.setx(brick.getx()+1)
            if paddle.getgrab() == False:
                ball.start_motion()
        display.object_render(paddle)
        display.object_render(ball)
        temp=0
        for brick in Breakable:
            if brick.getstatus() == True:
                display.object_render(brick)
            if powerup_list[temp] != None:
                if brick.getreleased()==True and brick.getreceived()==False:
                    if powerup_list[temp].getx()<=rows-5:
                        display.object_render(powerup_list[temp])
            temp = temp + 1
        for brick in Unbreakable:
            if brick.getstatus() == True:
                display.object_render(brick)
        for brick in Rainbow:
            if brick.getstatus() == True:
                display.object_render(brick)
            if powerup_list[temp] != None:
                if brick.getreleased()==True and brick.getreceived()==False:
                    if powerup_list[temp].getx()<=rows-5:
                        display.object_render(powerup_list[temp])
            temp = temp + 1
        level_finished = True
        for brick in Breakable:
            if brick.getstatus() == True:
                level_finished = False
        for brick in Unbreakable:
            if brick.getstatus() == True:
                level_finished = False
        for brick in Rainbow:
            if brick.getstatus() == True:
                level_finished = False
        if level_finished == True:
            level = level + 1
        display.render(lives,total_score(life_score)+ball.getscore(),round(begin,2))
    life_score.append(ball.getscore())
    lives = lives - 1