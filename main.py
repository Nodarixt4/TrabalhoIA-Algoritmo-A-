import numpy as np
from scipy.signal import convolve2d as conv2
import matplotlib
from queue import PriorityQueue

########################################################################################

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

        print(f"Estado == {numeroObservado}")
        print(f"Diferença: {diferencaDeEstados}")

    print(f"Distância Manhattan Total: {totalDiferenca}")
    return totalDiferenca

#manhattan()
#def avaliacao(custoAteAqui, custoAteFinal = manhattan()):
 #   custoTotal = custoAteAqui + custoAteFinal

    