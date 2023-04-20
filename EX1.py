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

    def setcolor(self,color):
        self.color = color

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        posmousex , posmousey = pg.mouse.get_pos()
        if posmousex>= self.x and posmousex <= self.w + self.x and posmousey >= self.y and posmousey <= self.h + self.y:
            return True
        else:
            return False
        
    def MousePressed(self):
        posmousex , posmousey = pg.mouse.get_pos()
        if posmousex>= self.x and posmousex <= self.w + self.x and posmousey >= self.y and posmousey <= self.h + self.y:
            if pg.mouse.get_pressed() == (1, 0, 0):
                return True
        else:
            return False

        

    
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn():
        if btn.MousePressed():
            btn.setcolor('blueviolet')
        else:
            btn.setcolor('cornsilk4')

    else:
        btn.setcolor('red')
    
    btn.draw(screen)

    
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False


