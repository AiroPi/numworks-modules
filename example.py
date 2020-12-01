# The game can be found here, if you want to test it with better performance on your numworks !
# https://workshop.numworks.com/python/airopi/snake

from kandinsky import *
from time import sleep
from ion import *
from random import randint

fill_rect(0,0,320,6,color(255,50,50))
fill_rect(0,0,5,222,color(255,50,50))
fill_rect(320-5,0,5,222,color(255,50,50))
fill_rect(0,222-6,320,6,color(255,50,50))

class Snake:
  def __init__(self):
    self.direction="up"
    self.tdirection="up"
  
    self.x,self.y=160,110
    self.len=3
    self.body=[(self.x,self.y)]
    self.sleep=0.0075
    self.inc=1

    self.eat = []
    for _ in range(3):
      self.spawn_food()

  def spawn_food(self):
    while True:      
      fx=randint(10,310)
      fy=randint(10,210)
      fx-=fx%10
      fy-=fy%10
      if (fx, fy) not in self.body:
        break
    fill_rect(int(fx-10/2),int(fy-10/2)+1,int(10),int(10),color(255,100,100))

    self.eat.append((fx, fy))

snk = Snake()
def show_score(sx=205,sy=6):
  draw_string("Score : {:0>2}".format(snk.len-3),sx,sy)  
show_score()

sub_iter = lambda i1, i2 : tuple(v1-v2 for v1, v2 in zip(i1,i2))

while True:
  if snk.len < len(snk.body):
    dx,dy=snk.body.pop(0)
  dx,dy=snk.body[0]  
  fill_rect(int(dx-10/2),int(dy-10/2)+1,int(10),int(10),color(255,255,255))

  fill_rect(int(snk.x-10/2),int(snk.y-10/2)+1,int(10),int(10),color(0,0,0))
  sleep(snk.sleep)

  if keydown(KEY_UP):
    snk.tdirection="up"
  if keydown(KEY_DOWN):
    snk.tdirection="down"
  if keydown(KEY_RIGHT):
    snk.tdirection="right"
  if keydown(KEY_LEFT):
    snk.tdirection="left"

  if snk.tdirection=="up" and snk.direction!="down" and snk.x%10==0:
    snk.direction="up"
  if snk.tdirection=="down" and snk.direction!="up" and snk.x%10==0:
    snk.direction="down"
  if snk.tdirection=="right" and snk.direction!="left" and snk.y%10==0:
    snk.direction="right"
  if snk.tdirection=="left" and snk.direction!="right" and snk.y%10==0:
    snk.direction="left"
    
  if snk.direction=="up":
    snk.y-=snk.inc
  if snk.direction=="down":
    snk.y+=snk.inc
  if snk.direction=="right":
    snk.x+=snk.inc
  if snk.direction=="left":
    snk.x-=snk.inc

  if snk.x%10==0 and snk.y%10==0:
    snk.body.append((snk.x,snk.y))
    if (snk.x,snk.y) in snk.eat:
      snk.len+=1
      del snk.eat[snk.eat.index((snk.x,snk.y))]
      
      snk.spawn_food()
      show_score()
      if snk.sleep>0.0005:
        snk.sleep-=0.0005
      elif snk.inc==1:
        snk.sleep=0.01
        snk.inc=2
      
    elif (snk.x,snk.y) in snk.body[:-1] or not 0<snk.x<320 or not 0<snk.y<220:
      fill_rect(5,6,310,210,color(255,255,255))
      draw_string("Game Over",120,100)
      draw_string("Press EXE to play again",55,120)
      
      high_score=0
      draw_string("Highscore : "+str(max(snk.len-3, high_score)),80,190)

      show_score(120,170)
      while not keydown(KEY_EXE):
        sleep(0.01)
      fill_rect(5,6,310,210,color(255,255,255))
      snk.__init__()
      show_score()
