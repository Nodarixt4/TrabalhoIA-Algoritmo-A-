import numpy as np
from scipy.signal import convolve2d as conv2
import matplotlib
from queue import PriorityQueue

########################################################################################

import movimentosValidos as movValidos
import manhattan as mh
import gerarMovimento as gMov

########################################################################################

contador = 0

matrizObjetivo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrizAtual = [
    [3, 5, 1],
    [7, 6, 2],
    [9, 8, 4]
]

memoriaMatrizes = []
memoriaMatrizes.extend(matrizAtual)


gMov.gerarMovimento(memoriaMatrizes,matrizObjetivo)


#for item in memoriaMatrizes:
#    print(memoriaMatrizes)

