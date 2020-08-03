import time
import operator
from dino import Dino
from random import randint
from numpy import std 


CONST_NUMD = 300
CONTS_XINI = 50
CONTS_YINI = 300
CONTS_MAX_HIGHT = 285
CONTS_GRAV = 0.25
CONTS_CHARH = 40
CONTS_CHARL = 43


class NNDino(Dino):
    # recebe o objeto
    # recebe parametros que decidem qual atitude deve ser tomada,
    # sao quatro listas que tem 2 parametros diferentes cada, sendo que eles variam de -1000 a mais 1000
    # paramN0  e paramN1 sao listas que sao parametros de tamanho 2 sao multiplixadores do output do neuronio 1 e 2
    def __init__(self, paramD, paramH, paramV, paramN0, paramN1):
        super(NNDino,self).__init__()
        
        self.dis = 0
        self.hig = 0
        self.vel = 4

        self.pd = paramD
        self.ph =  paramH
        self.pv = paramV
        self.n0 =  paramN0
        self.n1 = paramN1
    

    
    # os neuronios fazem o trabalho de um neuronio normal fazendo a soma
    def Neuron0(self):
        retorno = (self.dis * self.pd[0]) + (self.hig * self.ph[0])  + (self.vel * self.pv[0]) 
        if retorno <= 0:
            return 0
        return retorno
    def Neuron1(self):
        retorno = (self.dis * self.pd[1]) + (self.hig * self.ph[1])  + (self.vel * self.pv[1])
        if retorno <= 0:
            return 0
        return retorno
    def Neuron2(self):    
        return (self.Neuron0() * self.n0[0]) + (self.Neuron1() * self.n1[0])
    
    def Neuron3(self):    
        return (self.Neuron0() * self.n0[1]) + (self.Neuron1() * self.n1[1])

    # atualiza os parametros entre objeto e o dino
    # observe que o objeto deve estar a frente do dino
    def atualizaDAVL(self, obj, velo):
        if obj is None:
            return
        if 1 <= obj.type and obj.type <= 3:
            self.hig = 315 - obj.y
        else : 
            self.hig = 300 - obj.y

        self.dis = obj.x - self.x
        self.vel = velo

    def Decide(self, obj, velo):
        #verifica se a saida do neuronio 3 foi maior que a do neuronio 4, se tiver sido pede para pular
        # caso contrario abaixa
        self.atualizaDAVL(obj, velo)
        if self.Neuron2() >= self.Neuron3():
            self.atualiza(True, False)
        else:
            self.atualiza(False, True)
    
# cria inicialmente os dinossalros
def createFirstDinos():    
    dinos = []
    for i in range(0, CONST_NUMD) : 
        paramD = [randint(-1000, 1000),randint(-1000,1000)]
        paramH = [randint(-1000, 1000),randint(-1000,1000)]
        paramV = [randint(-1000, 1000),randint(-1000,1000)]
        paramN0 = [randint(-1000, 1000),randint(-1000,1000)]
        paramN1 = [randint(-1000, 1000),randint(-1000,1000)]
        dinos.append( NNDino(paramD, paramH, paramV, paramN0, paramN1))
    return dinos

        
# evolui apartir dos 10 caras mais bem sucedidios:
# usando o desvio padrao entre os dados dos mais sucedidos
def evolve(dinos):
    # ordena pela pontuacao apartir da maior pontuacao para a menor
    dinos.sort(key=operator.attrgetter('ponto'), reverse=True)
    print("ponto do dino0 :" ,dinos[0].ponto)
    print("ponto do ultimo dino :" ,dinos[CONST_NUMD - 1].ponto)

    # gera novos parametros apartir dos mais sucedidos usando o disvio padrao dos 10 primeiros
    if dinos[0].ponto < 10:
        stddD0 = stddD1 = stddD1 = stddH0 = stddH1= stddV0= stddV1= stddN00 = stddN01 = stddN10 = stddN11 \
        = int(10/dinos[0].ponto) * 10
    else :
        stddD0  =  int(std([dinos[i].pd[0]  for i in range(100)]))
        stddD1  =  int(std([dinos[i].pd[1]  for i in range(100)]))
        
        stddH0  =  int(std([dinos[i].ph[0]  for i in range(100)]))
        stddH1  =  int(std([dinos[i].ph[1]  for i in range(100)]))
        
        stddV0  =  int(std([dinos[i].pv[0]  for i in range(100)]))
        stddV1  =  int(std([dinos[i].pv[1]  for i in range(100)]))
        
        stddN00 =  int(std([dinos[i].n0[0] for i in range(100)]))
        stddN01 =  int(std([dinos[i].n0[1] for i in range(100)]))
        
        stddN10 =  int(std([dinos[i].n1[0] for i in range(100)]))
        stddN11 =  int(std([dinos[i].n1[1] for i in range(100)]))
    
    # gera novos dinossalros com carater semelhante a partir do dino mais sucedido
    # e a sdd entre os 10 mais sucedidos
    dinos[CONST_NUMD - 1] = dinos[0]
    for i in range(CONST_NUMD - 1):
        paramD = (dinos[0].pd[0] + randint(-stddD0, stddD0), dinos[0].pd[1] + randint(-stddD1,stddD1))
        paramH = (dinos[0].ph[0] + randint(-stddH0, stddH0),dinos[0].ph[1] + randint(-stddH1,stddH1))
        paramV = (dinos[0].pv[0] + randint(-stddV0, stddV0),dinos[0].pv[1] + randint(-stddV1,stddV1))
        paramN0 = (dinos[0].n0[0] + randint(-stddN00, stddN00),dinos[0].n0[1] + randint(-stddN01,stddN01))
        paramN1 = (dinos[0].n1[0] + randint(-stddN10, stddN10),dinos[0].n1[1] + randint(-stddN11,stddN11))
        dinos[i] =  NNDino(paramD, paramH, paramV, paramN0, paramN1)
def copyParam(dino1, dino2):
    dino1.pd[0] = dino2.pd[0]
    dino1.pd[1] = dino2.pd[1]

    dino1.ph[0] = dino2.ph[0]
    dino1.ph[1] = dino2.ph[1]

    dino1.pv[0] = dino2.pv[0]
    dino1.pv[1] = dino2.pv[1]

    dino1.n0[0] = dino2.n0[0]
    dino1.n0[1] = dino2.n0[1]

    dino1.n1[0] = dino2.n1[0]
    dino1.n1[1] = dino2.n1[1]

def changeAll(dinos, i ,var):
    dinos[i].pd[0] += randint(-var, var)
    dinos[i].pd[1] += randint(-var, var)
    dinos[i].ph[0] += randint(-var, var)
    dinos[i].ph[1] += randint(-var, var)
    dinos[i].pv[0] += randint(-var, var)
    dinos[i].pv[1] += randint(-var, var)
    dinos[i].n0[0] += randint(-var, var)
    dinos[i].n0[1] += randint(-var, var)
    dinos[i].n1[0] += randint(-var, var)
    dinos[i].n1[1] += randint(-var, var)
def lessThan5(dinos):
    var = 100
    for i in range(int(CONST_NUMD / 30), CONST_NUMD):
        dinos[i].heroesNeverDie()
        dinos[i].pd = [randint(-1000, 1000),randint(-1000,1000)]
        dinos[i].pv = [randint(-1000, 1000),randint(-1000,1000)]
        dinos[i].ph = [randint(-1000, 1000),randint(-1000,1000)]
        dinos[i].n0 = [randint(-1000, 1000),randint(-1000,1000)]
        dinos[i].n1 = [randint(-1000, 1000),randint(-1000,1000)]
    for i in range(int(CONST_NUMD/30)):
        dinos[i].heroesNeverDie()    


def lessThan20(dinos):
    var =  int(20 / dinos[0].ponto) * 10

    for i in range(1 , CONST_NUMD):
        dinos[i].heroesNeverDie()
        copyParam(dinos[i], dinos[0])
        if i % 5 == 0:
            dinos[i].pd[0] += randint(-var, var)
            dinos[i].pd[1] += randint(-var, var)
            dinos[i].ph[0] += randint(-var, var)
            dinos[i].ph[1] += randint(-var, var)

        elif i % 5 == 1:
            dinos[i].pv[0] += randint(-var, var)
            dinos[i].pv[1] += randint(-var, var)
            dinos[i].ph[0] += randint(-var, var)
            dinos[i].ph[1] += randint(-var, var)

        elif i % 5 == 2:
            dinos[i].pd[0] += randint(-var, var)
            dinos[i].pd[1] += randint(-var, var)
            dinos[i].pv[0] += randint(-var, var)
            dinos[i].pv[1] += randint(-var, var)
        elif i % 5 == 3:
            dinos[i].n0[0] += randint(-var, var)
            dinos[i].n0[1] += randint(-var, var)
            dinos[i].n1[0] += randint(-var, var)
            dinos[i].n1[1] += randint(-var, var) 
        else:
            changeAll(dinos, i, var)
            
def lessThan40(dinos):
    var =  int(200 / dinos[0].ponto) * 30

    for i in range(1 , CONST_NUMD):
        dinos[i].heroesNeverDie()
        copyParam(dinos[i], dinos[0])
        if i % 20 == 0:
            dinos[i].pd[0] += randint(-var, var)
            dinos[i].ph[1] += randint(-var, var)

        elif i % 20 == 1:
            dinos[i].pd[1] += randint(-var, var)
            dinos[i].ph[0] += randint(-var, var)

        elif i % 20 == 2:
            dinos[i].pd[0] += randint(-var, var)
            dinos[i].pv[1] += randint(-var, var)

        elif i % 20 == 3:
            dinos[i].pd[1] += randint(-var, var)
            dinos[i].pv[0] += randint(-var, var)

        elif i % 20 == 4:
            dinos[i].pv[1] += randint(-var, var)
            dinos[i].ph[0] += randint(-var, var)

        elif i % 20 == 5:
            dinos[i].pv[0] += randint(-var, var)
            dinos[i].ph[1] += randint(-var, var)

        elif i % 20 == 6:
            dinos[i].n0[0] += randint(-var, var)
            dinos[i].n1[1] += randint(-var, var)

        elif i % 20 == 7:
            dinos[i].n0[1] += randint(-var, var)
            dinos[i].n1[0] += randint(-var, var)
            
        else:
            changeAll(dinos, i, var)

def infinit(dinos):
    var = 10

    for i in range(1 , CONST_NUMD):
        dinos[i].heroesNeverDie()
        copyParam(dinos[i], dinos[0])
        if i % 3 == 0:
            dinos[i].pd[0] += randint(-var, var)
        elif i % 10 == 1:
            dinos[i].pd[1] += randint(-var, var)
        elif i % 10 == 2:
            dinos[i].ph[0] += randint(-var, var)
        elif i % 10 == 3:
            dinos[i].ph[1] += randint(-var, var) 

        elif i % 10 == 4:
            dinos[i].pv[0] += randint(-var, var)    
        elif i % 10 == 5:
            dinos[i].pv[1] += randint(-var, var)  

        elif i % 10 == 6:
            dinos[i].n0[1] += randint(-var, var)    
        elif i % 10 == 7:
            dinos[i].n0[0] += randint(-var, var)  

        elif i % 10 == 8:
            dinos[i].n1[1] += randint(-var, var)    
        else :
            dinos[i].n1[0] += randint(-var, var) 
    

def evolve2(dinos):
    # ordena pela pontuacao apartir da maior pontuacao para a menor
    dinos.sort(key=operator.attrgetter('ponto'), reverse=True)
    print("ponto do dino0 :" , dinos[0].ponto)
    print("ponto do ultimo dino :" , dinos[CONST_NUMD - 1].ponto)
    
    if  dinos[0].ponto <= 10:
        lessThan5(dinos)
    elif dinos[0].ponto <= 20:
        lessThan20(dinos)
    elif dinos[0].ponto <= 40:
        lessThan40(dinos)
    else:
        infinit(dinos)
    dinos[0].heroesNeverDie()

