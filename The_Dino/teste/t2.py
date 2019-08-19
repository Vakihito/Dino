import pygame 
import time
from dino import Dino
from cactus import Cactus
from bird import Bird
from random import randint
from time import clock

CONTS_XINI = 50
CONTS_YINI = 300
CONTS_MAX_HIGHT = 285
CONTS_GRAV = 0.25
CONTS_CHARH = 40
CONTS_CHARL = 43
CONTS_DOWN = 15

CONTS_XWIN = 720
CONTS_YWIN = 450

#verifica se apertou o botao de fechar o programa

def check_if_quit():
    for event in pygame.event.get():    #list the events and checks if it's 
        if event.type == pygame.QUIT:
            return False
    return True

pygame.init() #inicializando jogo

velX = 4
floor = pygame.image.load('chao0.png')
back = pygame.image.load('chao4.bmp')

#1600 de largura por 600 de altura
win = pygame.display.set_mode((CONTS_XWIN,CONTS_YWIN))
win.fill((255,255,255)) #fills with wight
pygame.display.set_caption("first Game")

dino1 = Dino()

tempoIni = clock()

run = True

lista = []

flag = False

def drawBackGround():
    win.fill((255,255,255)) #fills with wight
    
    for i in range(0, CONTS_XWIN, 60):
        win.blit(floor, (i , CONTS_YINI + CONTS_CHARH))





def redrawGameWindow():
    drawBackGround()
    #desenhando dino
    dino1.draw(win)
    for i in lista:
        i.draw(win)
    
    
    pygame.display.update()

# cria novo perigo
def createNewP(vel , lista, x):
    if randint(0,7) < 5:
            lista.append(Cactus(randint(0, 4) ,vel, x))
    else:
        lista.append(Bird(vel, x))

# spawna os perigos como passaro, cactus entre outros
# recebe uma lista de perigos que e a velocidade do jogo
def spawnP(vel, lista):

    # retira da lista caso o perigo tenha chegado ao fim
    for i in range(0, len(lista) - 1):
        if lista[i].x + lista[i].l <= 0:
            lista.pop(i)
        
    
    # caso sem nenhum obstaculo na tela
    if len(lista) == 0:
        createNewP(vel, lista, CONTS_XWIN)
    
    # se a distancia do ultimo perigo criado do ponto do spawn for maior que 
    # a velocidade do cenario vezes o tempo de queda do boneco tem uma chance
    # de criar um novo objeto
    distanciaProvavel = 90 # distancia minima para o pulo vezes a velocidade
    spawnPossivel = 50 # regiao onde o perigo pode surgir
    #         0 : (90, 90), 1 : (80, 50), 2 : (70, 40), 3 : (60, 30), 4 : (50, 20), 5 : (40, 10)

    swc = {
        0 : (60, 90, 100), 1 : (50 , 60, 40), 2 : ( 45 , 55, 40), 3 : (40, 50, 100), 4 : (35 , 40, 100), 5 : (20 ,40, 60)
    }

    # retirar isso apos implementacao da saida do programa
    if vel < 4:
        return
    if ((CONTS_XWIN - lista[len(lista) - 1].x) >= vel * randint(swc[int(vel - 4)][0],swc[int(vel - 4)][1])) and vel < 9:
        createNewP(vel, lista, randint(CONTS_XWIN, CONTS_XWIN + swc[int(vel - 4)][2]))

    
    
#recebe a lista de perigos e atualiza a velocidade dos objetos
def atualizaVelo(velX, lista):
    for i in lista:
        i.velX = velX 

# verifica se ocorreu uma colisao, se tiver ocorrido retorna True se nao retorna False
def checkIfHit(lista):
    
    for i in lista:
        if i.atualiza(dino1.hitBox, velX) :
            return True
    return False





def runTheGame():
    velX = 4
    run = True
    
    while run:
        pygame.time.delay(10) #delay da imagem
        
        run = check_if_quit()
        keys = pygame.key.get_pressed()#tecla selecionada
        
        dino1.atualiza(keys[pygame.K_UP], keys[pygame.K_DOWN]) 
        if checkIfHit(lista):
            velX = 0
            dino1.kill(tempoIni)
            run = False
        spawnP(velX, lista)
        
        if velX < 8:
            velX = 4 + (int(clock() - tempoIni) * 0.05)
        print(velX)
        
        atualizaVelo(velX, lista)
        

        redrawGameWindow()



runTheGame()
print(dino1.ponto)
pygame.quit()