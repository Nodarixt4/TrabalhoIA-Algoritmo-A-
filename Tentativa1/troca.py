import Tentativa1.posicaoDeAcordoComAposicao9 as pos

def troca(movimento,matriz):
    

    print(matriz)
    x,y = movimento
    a,b = pos.posicaoDeAcordoComAposicaoDo9(matriz)

    novaMatriz = matriz
    novaMatriz[a][b] = matriz[x][y]
    novaMatriz[x][y] = matriz[a][b]

    return novaMatriz