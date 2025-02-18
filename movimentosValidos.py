

def movimentosValidos(x, y, matrizAtual):
    movimentos = []
    
    if x < 0 or x >= len(matrizAtual) or y < 0 or y >= len(matrizAtual[0]):
        return movimentos
    
    if x > 0:
        movimentos.append((x - 1, y))
        print("cima")
    
    if x < len(matrizAtual) - 1:
        movimentos.append((x + 1, y))  
        print("baixo")
    
    if y > 0:
        movimentos.append((x, y - 1)) 
        print("esquerda")
    
    if y < len(matrizAtual[0]) - 1:
        movimentos.append((x, y + 1))  
        print("direita")
    
    return movimentos

#print("Movimentos Possiveis: ")
#movValidos.movimentosValidos(x, y, matrizRandom)