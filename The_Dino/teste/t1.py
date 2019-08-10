import pygame 
import time

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

#verifica os dados durante o pulo
def on_jump(char_y, vel_y):
    #verifica se esta no ar
    if char_y < CONTS_MAX_HIGHT : 
        if keys[pygame.K_DOWN]:
            return vel_y + 0.5
        return vel_y + 0.25
    return vel_y


# reseta as variaveis de posicao em relacao a y se estiver a baixo do solo
# verifica se esta apertando para ir para baixo se estiver abaixo do solo
# e abaixa o boneco
def reset(char_y, vel_y, char_hight):
    if char_y >= CONTS_YINI:
        if keys[pygame.K_DOWN]:
            return(CONTS_YINI + CONTS_DOWN, 0, CONTS_CHARH - CONTS_DOWN)
        return (CONTS_YINI, 0, CONTS_CHARH)
    return (char_y, vel_y, char_hight)




pygame.init() #inicializando jogo

walkDino = [pygame.image.load('dino0.jpg'), pygame.image.load('dino1.jpg'),
            pygame.image.load('dino2.jpg'), pygame.image.load('dino3.jpg'),
            pygame.image.load('dino4.jpg')]
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

def drawDino():

    #pulando
    if char_y < CONTS_MAX_HIGHT :
        win.blit(walkDino[4], (char_x, char_y))
        return
    if char_hight < CONTS_CHARH:
        if int((time.clock() * 10) % 2) == 0:
            win.blit(walkDino[2], (char_x, char_y))
            return
        
        win.blit(walkDino[3], (char_x, char_y))
        return

    if int((time.clock() * 10) % 2) == 0:
        win.blit(walkDino[0], (char_x, char_y))
        return

    win.blit(walkDino[1], (char_x, char_y))

def drawBackGround():
    win.fill((255,255,255)) #fills with wight
    
    for i in range(0, 1200,60):
        win.blit(floor, (i , CONTS_YINI + CONTS_CHARH))



def redrawGameWindow():

    drawBackGround()
    #desenhando dino
    drawDino()


    pygame.display.update()

run = True



while run:
    pygame.time.delay(10) #delay da imagem
    
    run = check_if_quit()

    keys = pygame.key.get_pressed()#tecla selecionada

    #e verifica se esta apertando para cima verifica se 250 <= char_y <= 300, espaco de pulo
    if keys[pygame.K_UP] and char_y <= CONTS_YINI and char_y >= CONTS_MAX_HIGHT:
        vel_y -= 2
   
    #verifica se esta no pulo                                  
    vel_y = on_jump(char_y, vel_y)

    #atualiza a posicao de acordo com a velocidade
    char_y += vel_y

    
    (char_y, vel_y, char_hight) = reset(char_y, vel_y, char_hight)
    redrawGameWindow()
    

pygame.quit()
    
    
