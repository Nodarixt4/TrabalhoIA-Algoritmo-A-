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
    numeroObservado = 1

    for posicao1 in range(len(matrizRandom)):
        for posicao2 in range(len(matrizRandom[posicao1])):
            if numeroObservado == matrizObjetivo[posicao1][posicao2]: 
                posicaoX1 = posicao1
                posicaoY1 = posicao2  
                
                for posicaoA in range(len(matrizObjetivo)):
                    for posicaoB in range(len(matrizObjetivo[posicaoA])):
                        if numeroObservado == matrizObjetivo[posicaoA][posicaoB]:  
                            posicaoX2 = posicaoA
                            posicaoY2 = posicaoB 

                diferencaX = abs(posicaoX1 - posicaoX2)
                diferencaY = abs(posicaoY1 - posicaoY2)

                diferencaDeEstados = diferencaX + diferencaY
                print(f"Estado == {numeroObservado}")
                print(f"Diferença: {diferencaDeEstados}")

                numeroObservado += 1  

    return diferencaDeEstados if 'diferencaDeEstados' in locals() else 0 
#def avaliacao(custoAteAqui, custoAteFinal = manhattan()):
 #   custoTotal = custoAteAqui + custoAteFinal

    