import numpy as np
from scipy.signal import convolve2d as conv2
import matplotlib
from queue import PriorityQueue

########################################################################################
movimentos = 0

matrizObjetivo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrizRandom = [
    [1, 9, 3],
    [4, 2, 6],
    [7, 5, 8]
]


def posicaoInicialDeAcordoComAposicaoDo9(matriz):
    for a in range(len(matriz)): 
        for b in range(len(matriz[a])):
            if matriz[a][b] == 9:
                return a, b
    return None, None

x, y = posicaoInicialDeAcordoComAposicaoDo9(matrizRandom)
ultimo_movimento = None


def melhor_movimento(matriz):
    global ultimo_movimento
    x, y = posicaoInicialDeAcordoComAposicaoDo9(matriz)
    movimentos = movimentosValidos(x, y, matriz)

    # Filtra para evitar o movimento inverso
    if ultimo_movimento in movimentos:
        movimentos.remove(ultimo_movimento)

    if not movimentos:
        return None

    melhor_custo = float("inf")
    melhor_mov = None

    for mov_x, mov_y in movimentos:
        matriz_simulada = [linha[:] for linha in matriz]
        matriz_simulada[x][y], matriz_simulada[mov_x][mov_y] = matriz_simulada[mov_x][mov_y], matriz_simulada[x][y]

        g = custoAteAqui()
        h = manhattan(matriz_simulada)
        f = g + h

        if f < melhor_custo:
            melhor_custo = f
            melhor_mov = (mov_x, mov_y)

    return melhor_mov

def mover_para_melhor(matriz):
    global ultimo_movimento
    mov = melhor_movimento(matriz)
    if mov:
        x, y = posicaoInicialDeAcordoComAposicaoDo9(matriz)
        matriz[x][y], matriz[mov[0]][mov[1]] = matriz[mov[0]][mov[1]], matriz[x][y]
        ultimo_movimento = (x, y)  # Atualiza a última posição do "9"
        return matriz
    return None


def movimentosValidos(x, y, matriz):
    movimentos = []
    
    if x < 0 or x >= len(matriz) or y < 0 or y >= len(matriz[0]):
        return movimentos
    
    if x > 0:
        movimentos.append((x - 1, y))  
    
    if x < len(matriz) - 1:
        movimentos.append((x + 1, y))  
    
    if y > 0:
        movimentos.append((x, y - 1))  
    
    if y < len(matriz[0]) - 1:
        movimentos.append((x, y + 1))  
    
    return movimentos


def custoAteAqui():
    global movimentos
    movimentos += 1
    return movimentos


def manhattan(matriz):
    totalDiferenca = 0  

    for numeroObservado in range(1, 10): 
        posicaoX1, posicaoY1 = None, None 
        posicaoX2, posicaoY2 = None, None
        
        for posicao1 in range(len(matriz)): 
            for posicao2 in range(len(matriz[posicao1])):
                if matriz[posicao1][posicao2] == numeroObservado:
                    posicaoX1, posicaoY1 = posicao1, posicao2

                if matrizObjetivo[posicao1][posicao2] == numeroObservado:
                    posicaoX2, posicaoY2 = posicao1, posicao2

        diferencaX = abs(posicaoX1 - posicaoX2)
        diferencaY = abs(posicaoY1 - posicaoY2)
        diferencaDeEstados = diferencaX + diferencaY

        totalDiferenca += diferencaDeEstados  

    return totalDiferenca


print("Estado Inicial:")
for linha in matrizRandom:
    print(linha)
print("")

print("Resolução:")

jogadas = 0

while matrizRandom != matrizObjetivo:
    nova_matriz = mover_para_melhor(matrizRandom)
    if nova_matriz:
        jogadas += 1
        for linha in nova_matriz:
            print(linha)
        print("")
    else:
        print("Nenhum movimento possível!")
        break

# Exibe o número total de jogadas
print(f"Total de jogadas: {jogadas}")