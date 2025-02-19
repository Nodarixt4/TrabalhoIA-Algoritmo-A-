
def posicaoDeAcordoComAposicaoDo9(matrizAtual):

    for a in range(len(matrizAtual)): 
            for b in range(len(matrizAtual[a])):
                if matrizAtual[a][b] == 9:
                    x = a
                    y = b
    return x,y