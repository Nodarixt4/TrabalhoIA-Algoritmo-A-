def manhattan(matrizAtual, matrizObjetivo):
    totalDiferenca = 0  

    for numeroObservado in range(1, 10): #começo das considerações
    
        posicaoX1, posicaoY1 = None, None 
        posicaoX2, posicaoY2 = None, None
        
        for posicao1 in range(len(matrizAtual)): 
            for posicao2 in range(len(matrizAtual[posicao1])):
                if matrizAtual[posicao1][posicao2] == numeroObservado:
                    posicaoX1, posicaoY1 = posicao1, posicao2

                if matrizObjetivo[posicao1][posicao2] == numeroObservado:
                    posicaoX2, posicaoY2 = posicao1, posicao2

        
        diferencaX = abs(posicaoX1 - posicaoX2)
        diferencaY = abs(posicaoY1 - posicaoY2)
        diferencaDeEstados = diferencaX + diferencaY

        totalDiferenca += diferencaDeEstados  

        #print(f"Estado == {numeroObservado}")
        #print(f"Diferença: {diferencaDeEstados}")

    #print(f"Distância Manhattan Total: {totalDiferenca}")
    return totalDiferenca

#manhattan()