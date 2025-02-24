import numpy as np
import heapq

#################################################################################################
def gerarMatrizDesorganizada(seletor, matrizDeterminada):
    if seletor == 1:
        return np.random.permutation(9).reshape(3,3) #gerar a mtriz aleatória
    if seletor == 2:
        return np.array([[4, 1, 3],
                        [0, 2, 5],
                        [7, 8, 6]])
    if seletor == 3:
        return matrizDeterminada
    else:
        print("Opção inválida")
        return 404

def gerarMatrizObjetivo():
    return np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 0]])
#################################################################################################
def encontrarCoordenada(matriz, numero):
    for x in range(3):
        for y in range(3):
            if matriz[x, y] == numero:
                return x,y
    return -1
#################################################################################################
def manhattan(matrizAtual, matrizObjetivo):
    totalDiferenca = 0  

    #print("\nMatriz Atual:")
    #print(matrizAtual)
    #print("\nMatriz Objetivo:")
    #print(matrizObjetivo)

    for numeroObservado in range(1, 9):  # Ignora o 0
        posicaoX1, posicaoY1 = encontrarCoordenada(matrizAtual, numeroObservado)
        posicaoX2, posicaoY2 = encontrarCoordenada(matrizObjetivo, numeroObservado)

        diferencaX = abs(posicaoX1 - posicaoX2)
        diferencaY = abs(posicaoY1 - posicaoY2)
        diferencaDeEstados = diferencaX + diferencaY

        totalDiferenca += diferencaDeEstados  

        #print(f"Estado == {numeroObservado}")
        #print(f"Diferença: {diferencaDeEstados}")

    #print(f"Distância Manhattan Total: {totalDiferenca}")
    return totalDiferenca
#################################################################################################
def movimentosValidos(x, y):
    movimentos = []
    
    if x > 0: 
        movimentos.append((x - 1, y))
        #print("cima")
    if x < 2: 
        movimentos.append((x + 1, y))
        #print("baixo")
    if y > 0: 
        movimentos.append((x, y - 1))
        #print("esquerda")
    if y < 2: 
        movimentos.append((x, y + 1))
        #print("direita")
    
    return movimentos
#################################################################################################
def moverZero(matriz, x, y, novo_x, novo_y):
    novaMatriz = matriz.copy()
    novaMatriz[x, y], novaMatriz[novo_x, novo_y] = novaMatriz[novo_x, novo_y], novaMatriz[x, y] #parte q o Vitor explicou
    return novaMatriz
#################################################################################################
def AestralDosDeuses(matrizInicial):
    matrizObjetivo = gerarMatrizObjetivo()
    fronteira = []
    heapq.heappush(fronteira, (manhattan(matrizInicial, matrizObjetivo), 0, tuple(map(tuple, matrizInicial)), [])) #adiciona um novo elemento à fila de prioridade frontei
    visitados = set() #com busca rápida e n permite duplicadas
    
    while fronteira:
        _, g, matriz_tuple, caminho = heapq.heappop(fronteira)
        matriz = np.array(matriz_tuple)
        
        if np.array_equal(matriz, matrizObjetivo):
            return caminho
        
        x, y = encontrarCoordenada(matriz, 0)
        for novo_x, novo_y in movimentosValidos(x, y):
            novaMatriz = moverZero(matriz, x, y, novo_x, novo_y)
            novaMatrizTuple = tuple(map(tuple, novaMatriz))
            
            if novaMatrizTuple not in visitados:
                visitados.add(novaMatrizTuple)
                novoCaminho = caminho + [novaMatriz]
                heapq.heappush(fronteira, (g + 1 + manhattan(novaMatriz, matrizObjetivo), g + 1, novaMatrizTuple, novoCaminho))
    pass
######################################## CAMPO DE TESTE #########################################
