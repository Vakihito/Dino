import pygame 
import time
from dino import Dino

CONTS_XINI = 50
CONTS_YINI = 300
CONTS_MAX_HIGHT = 285
CONTS_GRAV = 0.5
CONTS_CHARH = 40
CONTS_CHARL = 43
CONTS_DOWN = 15

#verifica se apertou o botao de fechar o programa

def check_if_quit():
    for event in pygame.event.get():    #list the events and checks if it's 
        if event.type == pygame.QUIT:
            return False
    return True




pygame.init() #inicializando jogo


floor = pygame.image.load('chao0.png')
back = pygame.image.load('chao4.bmp')

#1600 de largura por 600 de altura
win = pygame.display.set_mode((1200,600))
win.fill((255,255,255)) #fills with wight
pygame.display.set_caption("first Game")

char_x = CONTS_XINI
char_y = CONTS_YINI

vel_x = 2
vel_y = 0

tempo_antes_pulo = 0

char_hight = CONTS_CHARH
char_lengh = CONTS_CHARL
tempo_ini = 0

dino1 = Dino(CONTS_XINI, CONTS_YINI, 0, CONTS_CHARH, CONTS_CHARL)

def drawBackGround():
    win.fill((255,255,255)) #fills with wight
    
    for i in range(0, 1200,60):
        win.blit(floor, (i , CONTS_YINI + CONTS_CHARH))



def redrawGameWindow():

    drawBackGround()
    #desenhando dino
    dino1.draw(win)


    pygame.display.update()

run = True



while run:
    pygame.time.delay(10) #delay da imagem
    
    run = check_if_quit()

    keys = pygame.key.get_pressed()#tecla selecionada

    #e verifica se esta apertando para cima verifica se 250 <= char_y <= 300, espaco de pulo
    dino1.Jump(keys[pygame.K_UP])
   
    #verifica se esta no pulo                                  
    dino1.on_jump(keys[pygame.K_DOWN])

    #atualiza a posicao de acordo com a velocidade
    dino1.atualizaVel()

    
    dino1.keepUP(keys[pygame.K_DOWN])
    redrawGameWindow()
    

pygame.quit()
    
    
