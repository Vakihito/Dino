import pygame 
import time

CONTS_XINI = 50
CONTS_YINI = 300
CONTS_MAX_HIGHT = 285
CONTS_GRAV = 0.5

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
            print("entrei aqui1")
            return vel_y + 0.5
        return vel_y + 0.25
    return vel_y

# reseta as variaveis de posicao em relacao a y se estiver a baixo do solo
# verifica se esta apertando para ir para baixo se estiver abaixo do solo
# e abaixa o boneco
def reset(char_y, vel_y, char_hight):

    if char_y >= CONTS_YINI:
        if keys[pygame.K_DOWN]:
            return(CONTS_YINI + 10, 0, 20)
        return (CONTS_YINI, 0, 30)
    return (char_y, vel_y, char_hight)



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
    win.fill((255,255,255)) #fills with wight
   
    # print(char_y)
    pygame.draw.rect(win, (255,0,0),(char_x,char_y,char_lengh,char_hight))
    pygame.display.update()


pygame.quit()
    
    
