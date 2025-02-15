import numpy as np
from scipy.signal import convolve2d as conv2
import matplotlib
from queue import PriorityQueue

########################################################################################

VariavelDeIniciarObagulho = 0

matrizObjetivo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrizRandom = [
    [3, 5, 1],
    [7, 6, 2],
    [9, 8, 4]
]


def posicaoIncialDeAcordoComAposicaoDo9():

    for a in range(len(matrizRandom)): 
            for b in range(len(matrizRandom[a])):
                if matrizRandom[a][b] == 9:
                    x = a
                    y = b
                    VariavelDeIniciarObagulho = 1
    return x,y

x,y = posicaoIncialDeAcordoComAposicaoDo9()




def gerarMoviment():

    if VariavelDeIniciarObagulho ==1:
        movimentosValidos()
    else:
        posicaoIncialDeAcordoComAposicaoDo9()

    return





def movimentosValidos(x, y, matrizRandom):
    movimentos = []
    
    if x < 0 or x >= len(matrizRandom) or y < 0 or y >= len(matrizRandom[0]):
        return movimentos
    
    if x > 0:
        movimentos.append((x - 1, y))
        print("cima")
    
    if x < len(matrizRandom) - 1:
        movimentos.append((x + 1, y))  
        print("baixo")
    
    if y > 0:
        movimentos.append((x, y - 1)) 
        print("esquerda")
    
    if y < len(matrizRandom[0]) - 1:
        movimentos.append((x, y + 1))  
        print("direita")
    
    return movimentos


print("Movimentos Possiveis: ")
movimentosValidos(x, y, matrizRandom)











def custoAteAqui():
    movimentos = 0
    movimentos += 1
    return movimentos

def manhattan():
    totalDiferenca = 0  

    for numeroObservado in range(1, 10): #começo das considerações
    
        posicaoX1, posicaoY1 = None, None 
        posicaoX2, posicaoY2 = None, None
        
        for posicao1 in range(len(matrizRandom)): 
            for posicao2 in range(len(matrizRandom[posicao1])):
                if matrizRandom[posicao1][posicao2] == numeroObservado:
                    posicaoX1, posicaoY1 = posicao1, posicao2

                if matrizObjetivo[posicao1][posicao2] == numeroObservado:
                    posicaoX2, posicaoY2 = posicao1, posicao2

        
        diferencaX = abs(posicaoX1 - posicaoX2)
        diferencaY = abs(posicaoY1 - posicaoY2)
        diferencaDeEstados = diferencaX + diferencaY

        totalDiferenca += diferencaDeEstados  

        #print(f"Estado == {numeroObservado}")
        #print(f"Diferença: {diferencaDeEstados}")

    #print(f"Distância Manhattan Total: {totalDiferenca}")
    return totalDiferenca

#manhattan()

#def avaliacao(custoAteAqui = custoAteAqui(), custoAteFinal = manhattan()):
#    custoTotal = custoAteAqui + custoAteFinal

    