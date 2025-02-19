import numpy as np
##########################################################################
import funcoes as fun
##########################################################################

matrizObjetivo = fun.gerarMatrizObjetivo()
matrizAtual = fun.gerarMatrizDesorganizada()













################## CAMPO DE TESTE #########################################

for linha in matrizAtual:
    print(linha)
print("\n")
for linha in matrizObjetivo:
    print(linha)


"""
manhattanTeste = fun.manhattan(matrizAtual,matrizObjetivo)
print(manhattanTeste)
"""

"""
x,y = fun.encontrarCoordenada((matrizAtual),0)
testeMovimentosPossiveis = fun.movimentosValidos(x,y,matrizAtual)
print(testeMovimentosPossiveis)
"""

"""
x,y = fun.encontrarCoordenada((matrizAtual),0)
movimentos = fun.movimentosValidos(x,y,matrizAtual)
for a,b in movimentos:
    memoriaMatrizes.append(fun.moverZero(matrizAtual,x,y,a,b))
#for matriz in memoriaMatrizes:
#    print(np.array_str(matriz)) 
"""

"""
testeBuscaMelhor = fun.buscarMelhorMovimento(matrizAtual,matrizObjetivo,0)
print(testeBuscaMelhor)
"""

"""
for i in range(1,20):
    matrizAtual = fun.irParaOmelhor(matrizAtual,matrizObjetivo)
    print(matrizAtual)
"""