import manhattan as mh
import movimentosValidos as movValidos

def gerarMovimento(contador, matrizRandom, matrizObjetivo):
    
    movValidos.movimentosValidos()

    for a in range(1,4):
        matrizTeste = []
        matrizTeste.append(mh.manhattan(matrizRandom, matrizObjetivo) + contador)
    for a in range(1,4):
        if matrizTeste[a] > matrizTeste[a-1]:
            melhorMovimento = matrizTeste[a]


    return
