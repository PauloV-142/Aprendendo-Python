import random

def gerar():
    '''Gera todo o tabuleiro com números aleatórios, por enquanto.'''
    matrix = []
    for i in range(9):
        linha = list(range(1,9))
        matrix.append(random.choices(linha, k=9))
        #matrix.append([""]*9)
    return matrix

def mostrar(matrix):
    '''Mostra o tabuleiro de uma maneira agradável.'''
    for linha in matrix:
        for item in linha:
            print(item, ' ', end= ' ')
        print()
        print()

def celula(matrix, n): # How delightful! And Scary!
    '''Retorna um dicionário com as cordenadas de cada valor numérico.\n
       Automaticamente pinta os números em conflito.'''
    celula = {}
    x = n % 3
    y = n // 3
    for linha in range(y*3, y*3+3):
        for item in range(x*3, x*3+3):
            try:
                celula[matrix[linha][item]] = celula[matrix[linha][item]] + [linha, item]
            except:
                celula[matrix[linha][item]] = [linha, item]
    return celula

def mostrarConflitos(celula, matrix):
    for i in celula:
        item = celula[i]
        if len(item) > 2:
            for coord in range(1,len(item),2):
                matrix[item[coord-1]][item[coord]] = f"\033[32m{matrix[item[coord-1]][item[coord]]}\033[0m"
    return matrix

tabuleiro = gerar()
mostrar(tabuleiro)
print('-'*33)

for i in range(9):
    tabuleiro = mostrarConflitos(celula(tabuleiro, i), tabuleiro)
mostrar(tabuleiro)