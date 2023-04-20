import sys
import pygame as pg

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

class InputNumberBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if event.unicode.isdigit() == True:
                        self.text += event.unicode
                    else:
                        pass
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.color = 'lightpink1'
    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))

    def setcolor(self,color):
        self.color = color

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def MousePressed(self):
        posmousex , posmousey = pg.mouse.get_pos()
        if posmousex>= self.x and posmousex <= self.w + self.x and posmousey >= self.y and posmousey <= self.h + self.y:
            if pg.mouse.get_pressed() == (1, 0, 0):
                return True
        else:
            return False

pg.init()

fontsirname = pg.font.Font('freesansbold.ttf', 20) # font and fontsize
textsirname = fontsirname.render('Sirname', True,"hotpink1") # (text,is smooth?,letter color,background color)
textRectsirname = textsirname.get_rect() # text size
textRectsirname.center = (400, 80)

fontlastname = pg.font.Font('freesansbold.ttf', 20) # font and fontsize
textlastname = fontlastname.render('Lastname', True,"hotpink1") # (text,is smooth?,letter color,background color)
textRectlastname = textlastname.get_rect() # text size
textRectlastname.center = (400, 180)

fontage = pg.font.Font('freesansbold.ttf', 20) # font and fontsize
textage = fontage.render('Age', True,"hotpink1") # (text,is smooth?,letter color,background color)
textRectage = textage.get_rect() # text size
textRectage.center = (400, 280)

font = pg.font.Font('freesansbold.ttf', 15) # font and fontsize
text = font.render('Hello {} {}! You are {} years old.', True,"hotpink1") # (text,is smooth?,letter color,background color)
textRect = text.get_rect() # text size
textRect.center = (380,400)
texton = False

win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(300, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(300, 200, 140, 32) # สร้าง InputBox2
input_box3 = InputNumberBox(300, 300, 140, 32) # สร้าง InputBox3
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

btn = Button(650,400,100,30) # สร้าง Object จากคลาส Button ขึ้นมา

while run:
    screen.fill((255, 255, 255))
    if btn.MousePressed():
        texton = True
        text = font.render('Hello {} {}! You are {} years old.'.format(input_box1.text,input_box2.text,input_box3.text), True,"hotpink1")
        btn.setcolor('deeppink1')
        
    else:
        btn.setcolor('lightpink1')
    
    if texton:
        screen.blit(text, textRect)
    
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    screen.blit(textsirname, textRectsirname)
    screen.blit(textlastname, textRectlastname)
    screen.blit(textage, textRectage)

    btn.draw(screen)
    pg.time.delay(1)
    pg.display.update()