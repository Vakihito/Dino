
import pygame
import time
from random import randint

CONTS_XINI = 720
CONTS_YINI = 270

CONTS_MAX_HIGHT = 285

CONTS_CHARL1 = 45
CONTS_CHARH1 = 36


birdImg = [pygame.image.load('passaro1.png'),
             pygame.image.load('passaro2.png')]

class Bird(object):
    def __init__(self, vel_x, posx = CONTS_XINI):
        self.x = posx
        num = randint(0, 2)
        if num == 0:
            self.y = 230
        elif num == 1:
            self.y = (300 + 230) / 2 
        else:
            self.y = 300
        self.velX = vel_x
        self.img, self.l, self.h = (birdImg[1], CONTS_CHARL1, CONTS_CHARH1)
        self.hitBox = (self.x + 4, self.y + 2, self.l - 12, self.h - 7)
        self.type = 5

    def move(self, vel_x):
        
        self.velX = vel_x
        self.x -= self.velX

    def atualizaHitBox(self):
        self.hitBox = (self.x + 4, self.y + 2, self.l - 12, self.h - 7)

    def drawHitBox(self, win):
        self.atualizaHitBox()
        pygame.draw.rect(win, (255,0,0), self.hitBox , 2)

    def draw(self, win):
        self.drawHitBox(win)
        
        if int((time.clock() * 10) % 2) == 0:
            self.img = birdImg[0]
        else:
            self.img = birdImg[1]
        win.blit(self.img, (self.x, self.y)) 

    

    def checkIfHits(self, coord):
        if (self.hitBox[1] < coord[1] + coord[3] and
            coord[1] < self.hitBox[1] + self.hitBox[3] and
            self.hitBox[0] < coord[0] + coord[2] and  
            coord[0] < self.hitBox[0] + self.hitBox[2]
            ):
            self.velX = 0
            return True
        return False

    # atualiza o movimento assim como verifica se acertou o dino
    def atualiza(self, coord, vel):
        self.move(self.velX)
        return self.checkIfHits(coord)
    
    
