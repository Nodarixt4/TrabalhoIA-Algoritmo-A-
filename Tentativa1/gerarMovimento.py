import Tentativa1.manhattan as mh
import Tentativa1.movimentosValidos as movValidos
import Tentativa1.posicaoDeAcordoComAposicao9 as pos 
import Tentativa1.troca as tr

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
