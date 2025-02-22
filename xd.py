import numpy as np

########################################################################################
movimentos = 0

matrizObjetivo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrizRandom = [
    [1, 2, 3],
    [4, 8, 6],
    [7, 5, 9]
]

# Armazena os estados já visitados para evitar loops
estados_visitados = set()


def posicaoInicialDeAcordoComAposicaoDo9(matriz):
    for a in range(len(matriz)): 
        for b in range(len(matriz[a])):
            if matriz[a][b] == 9:
                return a, b
    return None, None


def melhor_movimento(matriz):
    global movimentos, estados_visitados
    x, y = posicaoInicialDeAcordoComAposicaoDo9(matriz)
    movimentos_possiveis = movimentosValidos(x, y, matriz)

    if not movimentos_possiveis:
        return None

    melhor_custo = float("inf")
    melhor_mov = None

    for mov_x, mov_y in movimentos_possiveis:
        # Cria uma cópia da matriz e simula o movimento
        matriz_simulada = [linha[:] for linha in matriz]
        matriz_simulada[x][y], matriz_simulada[mov_x][mov_y] = matriz_simulada[mov_x][mov_y], matriz_simulada[x][y]

        # Converte a matriz para um formato imutável (tupla) para armazenar no set
        estado_atual = tuple(tuple(linha) for linha in matriz_simulada)
        if estado_atual in estados_visitados:
            continue  # Evita repetir estados

        g = movimentos + 1  # Custo do caminho até aqui
        h = manhattan(matriz_simulada)  # Estimativa de distância até a solução
        f = g + h  # Função de avaliação A*

        if f < melhor_custo:
            melhor_custo = f
            melhor_mov = (mov_x, mov_y)

    return melhor_mov


def mover_para_melhor(matriz):
    global movimentos, estados_visitados
    mov = melhor_movimento(matriz)

    if mov:
        x, y = posicaoInicialDeAcordoComAposicaoDo9(matriz)
        matriz[x][y], matriz[mov[0]][mov[1]] = matriz[mov[0]][mov[1]], matriz[x][y]
        
        # Armazena o estado atual no conjunto de estados visitados
        estado_atual = tuple(tuple(linha) for linha in matriz)
        estados_visitados.add(estado_atual)

        movimentos += 1
        return matriz
    return None


def movimentosValidos(x, y, matriz):
    movimentos = []
    
    if x > 0:
        movimentos.append((x - 1, y))  
    
    if x < len(matriz) - 1:
        movimentos.append((x + 1, y))  
    
    if y > 0:
        movimentos.append((x, y - 1))  
    
    if y < len(matriz[0]) - 1:
        movimentos.append((x, y + 1))  
    
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
