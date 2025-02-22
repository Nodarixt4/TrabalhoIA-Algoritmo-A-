import numpy as np

def gerarMatrizDesorganizada():
    matrizAtual = np.random.permutation(9).reshape(3,3)
    return matrizAtual

def gerarMatrizObjetivo():
    return np.array([[1, 2, 3],
                     [4, 5, 6], #meo deos, q formatação delicia
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

def movimentosValidos(x, y, matriz):
    movimentos = []
    
    if x < 0 or x >= len(matriz) or y < 0 or y >= len(matriz[0]):
        return movimentos
    
    if x > 0:
        movimentos.append((x - 1, y))
        #print("cima")
    
    if x < len(matriz) - 1:
        movimentos.append((x + 1, y))  
        #print("baixo")
    
    if y > 0:
        movimentos.append((x, y - 1)) 
        #print("esquerda")
    
    if y < len(matriz[0]) - 1:
        movimentos.append((x, y + 1))  
        #print("direita")
    print("\n")
    return movimentos

#################################################################################################

def moverZero(matriz, x, y, novo_x, novo_y):
    """
    Move o zero na matriz para a posição (novo_x, novo_y) e retorna uma nova matriz.
    """
    novaMatriz = matriz.copy()
    novaMatriz[x, y], novaMatriz[novo_x, novo_y] = novaMatriz[novo_x, novo_y], novaMatriz[x, y]
    return novaMatriz

#################################################################################################

def buscarMelhorMovimento(matrizAtual, matrizObjetivo,escolha):
    x, y = encontrarCoordenada(matrizAtual, 0)
    movimentos = movimentosValidos(x, y, matrizAtual)

    melhoresMovimentos = []
    for (novo_x, novo_y) in movimentos:
        novaMatriz = moverZero(matrizAtual, x, y, novo_x, novo_y)
        custo = manhattan(novaMatriz, matrizObjetivo)
        melhoresMovimentos.append((custo, novaMatriz))

    #tirada do GPT essa parte
    # Escolhe o movimento com o menor custo (menor distância Manhattan)
    melhoresMovimentos.sort(key=lambda x: x[0])  # Ordena por custo
    melhorCusto, melhorMatriz = melhoresMovimentos[0]

    if escolha == 0:
        return melhorMatriz
    else:
        return melhorCusto

#################################################################################################

def irParaOmelhor(matrizAtual,matrizObjetivo):
    matrizAtual = buscarMelhorMovimento(matrizAtual,matrizObjetivo,0)
    return matrizAtual

#################################################################################################

