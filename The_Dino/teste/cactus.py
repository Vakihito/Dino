
import pygame
import time

CONTS_XINI = 720
CONTS_YINI = 300

CONTS_MAX_HIGHT = 285

CONTS_CHARL1 = 25
CONTS_CHARH1 = 48

CONTS_CHARL2 = 18
CONTS_CHARH2 = 35

CONTS_CHARL3 = 35
CONTS_CHARH3 = 35

CONTS_CHARL4 = 52
CONTS_CHARH4 = 35

CONTS_CHARL5 = 75
CONTS_CHARH5 = 50


cactusImg = [pygame.image.load('cactusGrande1.png'), pygame.image.load('cactusPequeno1.png'),
             pygame.image.load('cactusPequeno2.png'), pygame.image.load('cactusPequeno3.png'),
             pygame.image.load('cactus4.png')]

class Cactus(object):
    def __init__(self, tipo, vel_x , posx = CONTS_XINI):
        self.x = posx
        self.y = CONTS_YINI
        if 1 <= tipo and tipo <=3:
            self.y += 15

        self.velX = vel_x
        self.type = tipo

        swt = {
            0 : (cactusImg[0], CONTS_CHARL1, CONTS_CHARH1),
            1 : (cactusImg[1], CONTS_CHARL2, CONTS_CHARH2),
            2 : (cactusImg[2], CONTS_CHARL3, CONTS_CHARH3),
            3 : (cactusImg[3], CONTS_CHARL4, CONTS_CHARH4),
            4 : (cactusImg[4], CONTS_CHARL5, CONTS_CHARH5)
        }
        self.img, self.l, self.h = swt[tipo]

        self.hitBox = (self.x , self.y, self.l - 6, self.h - 5)

    def move(self, vel_x):
       
        self.velX = vel_x
        self.x -= self.velX
        

    def atualizaHitBox(self):
        self.hitBox = (self.x, self.y, self.l - 6, self.h - 5)

    def drawHitBox(self, win):
        self.atualizaHitBox()
        pygame.draw.rect(win, (255,0,0), self.hitBox , 2)

    def draw(self, win):
        self.drawHitBox(win)
        win.blit(self.img, (self.x, self.y))

    

    def checkIfHits(self, coord):
        if (self.hitBox[1] < coord[1] + coord[3] and
            coord[1] < self.hitBox[1] + self.hitBox[3] and
            self.hitBox[0] < coord[0] + coord[2] and  
            coord[0] < self.hitBox[0] + self.hitBox[2]
            ):
            return True
        return False

    def atualiza(self, coord, vel):
        self.move(self.velX)
        return self.checkIfHits(coord)

    
    

