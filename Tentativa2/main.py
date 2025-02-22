import numpy as np
import funcoes as fun

##########################################################################
seletor = int(input("-1 Matriz inicial aleatória\n-2 Pré determinada \n-3 Escrever matriz \nResposta: "))

matrizDeterminada = np.zeros((3, 3), dtype=int)

if seletor == 3:
    for linha in range(matrizDeterminada.shape[0]):  
        for coluna in range(matrizDeterminada.shape[1]):  
            matrizDeterminada[linha, coluna] = int(input(f"Posição[{linha+1}][{coluna+1}]: "))

matrizInicial = fun.gerarMatrizDesorganizada(seletor, matrizDeterminada)
print("Matriz inicial:")
print(matrizInicial)

solucao = fun.AestralDosDeuses(matrizInicial)
if solucao:
    print("\nGarantido...", len(solucao), "movimentos e tá resolvido.")
    for passo, estado in enumerate(solucao):
        print("\nPasso", passo + 1)
        print(estado)
else:
    print("\nMoio...achei foi nothing!")
