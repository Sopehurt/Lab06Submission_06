import sys
import pygame as pg

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.color = 'red'
    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))
    
    


class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def movebutton(self,stepx,stepy):
        self.x = self.x + stepx
        self.y = self.y + stepy
    
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    btn.draw(screen)
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            print("Key D down")
            btn.movebutton(10,0)

        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            print("Key D down")
            btn.movebutton(0,10)

        if event.type == pg.KEYDOWN and event.key == pg.K_a:
            print("Key D down")
            btn.movebutton(-10,0)

        if event.type == pg.KEYDOWN and event.key == pg.K_w:
            print("Key D down")
            btn.movebutton(0,-10)

        if event.type == pg.QUIT:
            pg.quit()
            run = False

