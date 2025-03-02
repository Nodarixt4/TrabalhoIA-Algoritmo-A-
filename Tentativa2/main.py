import numpy as np
import funcoes as fun
import time

##########################################################################
seletor1 = int(input("-1 Matriz inicial aleatória\n-2 Pré determinada \n-3 Escrever matriz \nResposta: "))
seletor2 = int(input("Resolver com 1-Manhattan ou 0-Haming? "))
seletor3 = int(input("Com fila de prioridade?(1-sim/0-não): "))

matrizDeterminada = np.zeros((3, 3), dtype=int)

if seletor1 == 3:
    for linha in range(matrizDeterminada.shape[0]):  
        for coluna in range(matrizDeterminada.shape[1]):  
            matrizDeterminada[linha, coluna] = int(input(f"Posição[{linha+1}][{coluna+1}]: "))

matrizInicial = fun.gerarMatrizDesorganizada(seletor1, matrizDeterminada)
print("Matriz inicial:")
print(matrizInicial)
a=fun.ehresolvido(matrizInicial)

if a == 1:
    start_time = time.time()
    if seletor3==1:
        solucao = fun.AestralDosDeuses(matrizInicial,seletor2)
    if seletor3==0:
        solucao = fun.AestralDosDeusesSemFila(matrizInicial,seletor2)
    end_time = time.time()
    tempo_execucao = end_time - start_time
    print(f"Tempo de execução: {tempo_execucao:.4f} segundos")

    if solucao:
        print("\nGarantido...", len(solucao), "movimentos e tá resolvido.")
        for passo, estado in enumerate(solucao):
            print("\nPasso", passo + 1)
            print(estado)
    else:
        print("\nMoio...achei foi nothing!")

################################################################################

#E se eu tirar a fila de prioridade?

"""Se não utilizássemos uma fila de prioridade, perderíamos a principal vantagem do algoritmo A*, que é sempre expandir o estado com o menor custo estimado primeiro. Sem essa estrutura, poderíamos usar uma fila comum (FIFO) ou uma pilha"""

#Se demorar dms pra achar resultado, roda dnvkkkkkkk.  Ela ainda é muito mais "artificial" do  q "inteligente".