import random
def gerar():
    '''Gera todo o tabuleiro com números aleatórios, por enquanto.'''
    matrix = []
    for i in range(9):
        linha = list(range(1,9))
        matrix.append(random.choices(linha, k=9))
        #matrix.append([""]*9)
    return matrix

def mostrarTabuleiro(matrix):
    '''Mostra o tabuleiro de uma maneira agradável.'''
    for linha in matrix:
        for item in linha:
            print(item, ' ', end= ' ')
        print()
        print()

def celula(n): # How delightful! And Scary!
    '''Retorna uma lista com as cordenadas de cada valor da célula.'''
    celula = []
    x = n % 3
    y = n // 3
    for linha in range(y*3, y*3+3):
        for item in range(x*3, x*3+3):
            celula.append([linha, item])
    return celula

def mostrarConflitos(matrix):
    for p in range(9):
        cell = celula(p)
        cellVal = []
        for i in cell:
            cellVal.append(matrix[i[0]][i[1]])
        for i, val in enumerate(cellVal):
            if cellVal.count(val) > 1:
                coord = cell[i]
                matrix[coord[0]][coord[1]] = f"\033[32m{matrix[coord[0]][coord[1]]}\033[0m"
    return matrix

tabuleiro = gerar()

print('-'*33)

mostrarTabuleiro(mostrarConflitos(tabuleiro))