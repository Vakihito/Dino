import pygame 
import time

CONTS_XINI = 50
CONTS_YINI = 300
CONTS_MAX_HIGHT = 285
CONTS_GRAV = 0.5

pygame.init() #inicializando jogo



win = pygame.display.set_mode((1600,600))
pygame.display.set_caption("first Game")

char_x = CONTS_XINI
char_y = CONTS_YINI

vel_x = 2
vel_y = 0

tempo_antes_pulo = 0

char_hight = 30
char_lengh = 30
tempo_ini = 0

run = True

def check_if_quit():
    for event in pygame.event.get():    #list the events and checks if it's 
        if event.type == pygame.QUIT:
            return False
    return True


    

while run:
    pygame.time.delay(10) #delay da imagem
    
    # for event in pygame.event.get():    #list the events and checks if it's 
    #     if event.type == pygame.QUIT:
    #         run = False
    run = check_if_quit()
    keys = pygame.key.get_pressed()#tecla selecionada


    #e verifica se esta apertando para cima verifica se 250 <= char_y <= 300, espaco de pulo
    if keys[pygame.K_UP] and char_y <= CONTS_YINI and char_y >= CONTS_MAX_HIGHT:
        vel_y -= 2
   
    #verifica se esta no pulo                                  
    if char_y < CONTS_MAX_HIGHT :
        vel_y += 0.25
        if keys[pygame.K_DOWN]:
            vel_y += 0.5

    #atualiza a posicao de acordo com a velocidade
    char_y += vel_y

    if char_y >= 300:
        char_y = 300
        vel_y = 0
        char_hight = 30
        char_y = CONTS_YINI

        if keys[pygame.K_DOWN]:
            char_hight = 20
            char_y = CONTS_YINI + 10



    
    
    win.fill((255,255,255)) #fills with wight
   
    # print(char_y)
    pygame.draw.rect(win, (255,0,0),(char_x,char_y,char_lengh,char_hight))
    pygame.display.update()


pygame.quit()
    
    
