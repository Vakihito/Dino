import pygame
import time

CONTS_XINI = 50
CONTS_YINI = 300
CONTS_MAX_HIGHT = 285
CONTS_GRAV = 0.5
CONTS_CHARH = 40
CONTS_CHARL = 45
CONTS_DOWN = 15
CONTS_LDOW = 60



# imagens definidas
walkDino = [pygame.image.load('dino0.png'), pygame.image.load('dino1.png'),
            pygame.image.load('dino2.png'), pygame.image.load('dino3.png'),
            pygame.image.load('dino4.png')]

class Dino(object):
    def __init__(self):
        self.x = CONTS_XINI
        self.y = CONTS_YINI
        self.velY = 0
        self.h = CONTS_CHARH
        self.l =  CONTS_CHARL
        self.ponto = 0
        self.isVivo = True
        self.hitBox = (self.x + 6, self.y, self.l -16, self.h )
    
    # condicao de pulo
    def Jump(self, gojump):
        if gojump and self.y <= CONTS_YINI and self.y >= CONTS_MAX_HIGHT:
            self.velY -= 1.25
    def atualizaHitBox(self):
        self.hitBox = (self.x + 6, self.y, self.l - 16, self.h )


    def drawHibox(self, win):
        self.atualizaHitBox()
        pygame.draw.rect(win, (255,0,0), self.hitBox , 2)

    # mostra o dinossalro na tela
    def draw(self, win):

        if not self.isVivo:
            return
        
        self.drawHibox(win)

        # dino esta pulando
        if self.y < CONTS_MAX_HIGHT :
            win.blit(walkDino[4], (self.x, self.y))
            return

        # dino esta abaixado
        if self.h < CONTS_CHARH:
            if int((time.clock() * 10) % 2) == 0:
                win.blit(walkDino[2], (self.x, self.y))
                return
            win.blit(walkDino[3], (self.x, self.y))
            return

        # nao esta pulando esta no chao
        if int((time.clock() * 10) % 2) == 0:
            win.blit(walkDino[0], (self.x, self.y))
            return
        win.blit(walkDino[1], (self.x, self.y))

    #verifica os dados durante o pulo
    def on_jump(self, goDown):
        #verifica se esta no ar
        if self.y < CONTS_MAX_HIGHT : 
            #verifica esta tentando ir para baixo
            if goDown:
                self.velY += 0.75 # se estiver aumenta a velocidade de queda
                return

            self.velY += 0.25  # velocidade de queda eh 0.25
            return

        return

    #reseta status do dino
    def reset(self):
        self.y = CONTS_YINI
        self.velY = 0
        self.h = CONTS_CHARH
        self.l = CONTS_CHARL

    # caso o dino esteja so correndo 
    def keepUP(self, goDown):
        # se ele estiver a baixo do terreno ou em cima do terreno
        if self.y >= CONTS_YINI:

            if goDown: 
                self.y = CONTS_YINI + CONTS_DOWN
                self.velY = 0
                self.h = CONTS_CHARH - CONTS_DOWN
                self.l = CONTS_LDOW 
                return
            # reseta dados para o padrao
            self.reset()
            return

        return
    def atualiza(self, goUp, goDown):
        if not self.isVivo:
            return
            
        self.Jump(goUp)
        self.on_jump(goDown)
        self.y += self.velY
        self.keepUP(goDown)
    def kill(self, tempoI):
        self.isVivo = False
        self.velY = 0
        self.ponto = (time.clock() - tempoI)

    def heroesNeverDie(self):
        self.x = CONTS_XINI
        self.y = CONTS_YINI
        self.velY = 0
        self.h = CONTS_CHARH
        self.l =  CONTS_CHARL
        self.ponto = 0
        self.isVivo = True
        self.hitBox = (self.x + 6, self.y, self.l -16, self.h )
    