import pygame 
import time
from dino import Dino
from cactus import Cactus
from bird import Bird
from random import randint
from time import clock
from NNDino import NNDino
from NNDino import evolve
from NNDino import createFirstDinos


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
floor = pygame.image.load('chao0.png')  #carregando imagem do chao
back = pygame.image.load('chao4.bmp') 
#1600 de largura por 600 de altura
win = pygame.display.set_mode((CONTS_XWIN,CONTS_YWIN))   # desenhando a janela
win.fill((255,255,255))                                  # fills with wight

pygame.display.set_caption("Dino Neural Network")       # colocando o nome da janela
dinos = createFirstDinos()              # criando dinossalros
tempoIni = clock()                          # salvando tempo inicial da aplicacao
listap = []                                  # listap de Perigos


# desenha o back Ground
def drawBackGround():
    win.fill((255,255,255)) #fills with wight
    
    for i in range(0, CONTS_XWIN, 60):
        win.blit(floor, (i , CONTS_YINI + CONTS_CHARH))

# atualiza os quadros
def redrawGameWindow():
    drawBackGround()    
    # desenhando dinos
    for i in dinos:
        i.draw(win)

    for i in listap:
        i.draw(win)
    
    
    pygame.display.update()

# cria novo perigo
def createNewP(vel , listap, x):
    if randint(0,7) < 5:
            listap.append(Cactus(randint(0, 4) ,vel, x))
    else:
        listap.append(Bird(vel, x))

# spawna os perigos como passaro, cactus entre outros
# recebe uma listap de perigos que e a velocidade do jogo
def spawnP(vel, listap):

    # retira da listap caso o perigo tenha chegado ao fim
    for i in range(0, len(listap) - 1):
        if listap[i].x + listap[i].l <= 0:
            listap.pop(i)
        
    
    # caso sem nenhum obstaculo na tela
    if len(listap) == 0:
        createNewP(vel, listap, CONTS_XWIN)
    
    # se a distancia do ultimo perigo criado do ponto do spawn for maior que 
    # a velocidade do cenario vezes o tempo de queda do boneco tem uma chance
    # de criar um novo objeto
    distanciaProvavel = 90 # distancia minima para o pulo vezes a velocidade
    spawnPossivel = 50 # regiao onde o perigo pode surgir
    #         0 : (90, 90), 1 : (80, 50), 2 : (70, 40), 3 : (60, 30), 4 : (50, 20), 5 : (40, 10)

    swc = {
        0 : (60, 90, 100), 1 : (50 , 80, 40), 2 : ( 50 , 80, 40), 3 : (40, 80, 100), 4 : (40 , 80, 100), 5 : (20 ,30, 60)
    }

    # retirar isso apos implementacao da saida do programa
    if vel < 4:
        return
    if ((CONTS_XWIN - listap[len(listap) - 1].x) >= vel * randint(swc[int(vel - 4)][0],swc[int(vel - 4)][1])) and vel < 9:
        createNewP(vel, listap, randint(CONTS_XWIN, CONTS_XWIN + swc[int(vel - 4)][2]))

    
    
#recebe a listap de perigos e atualiza a velocidade dos objetos
def atualizaVelo(velX, listap):

    for i in listap:
        i.velX = velX 
        
    if velX < 8:
        return (4 + (int(clock() - tempoIni) * 0.05))
    return velX
# verifica se ocorreu uma colisao, se tiver ocorrido retorna True se nao retorna False
def checkIfHit(velX, listap):
    # percorre a lista de obstaculos e verifica se o dino sofreu hit
    for i in listap:
        i.move(velX)
        for d in dinos:
            if i.checkIfHits(d.hitBox) :
                d.kill(tempoIni)
                
    
# retorna o proximo objeto em frente ao dinossalro
def objInFront():
    for i in listap:
        if i.x >= CONTS_XINI :
            return i

# retorna True se tem pelo menos um dinossalro vivo
# se nao retorna Falso
def checkHaveOne():
    for i in dinos:
        if i.isVivo:
            return True
    return False

def runTheGame():
    velX = 4
    run = True
    
    while run:
        pygame.time.delay(10) #delay da imagem
        run = checkHaveOne() # verifica se saiu do game ou se tem um dinossalro vivo        
        if not check_if_quit():
            return False

        # os dinossalros tomam a decisao de pular ou abaixar
        for i in dinos:
            i.Decide(objInFront(), velX)

        checkIfHit(velX, listap) # ferifica se algum dino foi morto
        spawnP(velX, listap) # spawna mais perigos
        velX = atualizaVelo(velX, listap) # atualiza a velocidade do jogo

        redrawGameWindow()  # redesenha as coisas

    return True

flagOn = True
while flagOn:
    listap = []
    win.fill((255,255,255))                                  # fills with wight
    pygame.display.set_caption("Dino Neural Network")       # colocando o nome da janela
    tempoIni = clock() 


    
    flagOn = runTheGame()
    print(dinos[0].ponto)
    evolve(dinos) #evolui dos dinossalros
    
    

pygame.quit()