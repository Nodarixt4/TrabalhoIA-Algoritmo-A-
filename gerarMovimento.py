import manhattan as mh
import movimentosValidos as movValidos
import posicaoDeAcordoComAposicao9 as pos 
import troca as tr

def gerarMovimento(memoriaMatrizes, matrizObjetivo):
    i = 0
    for item in range(len(memoriaMatrizes)):
        x,y = pos.posicaoDeAcordoComAposicaoDo9(memoriaMatrizes[item])
        movimentos = movValidos.movimentosValidos(x,y,memoriaMatrizes[item])
        i += 1
    for item in range(len(movimentos)):
        novaMAtriz = tr.troca(movimentos[item],memoriaMatrizes[0])#conferir se o 'i' ta certo dps
        print(novaMAtriz)
    return
