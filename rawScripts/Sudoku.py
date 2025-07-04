'''Work In Progress...'''
import random
import tkinter as tk

def gerar():
    '''Gera todo o tabuleiro com números aleatórios, por enquanto.'''
    matrix = []
    for i in range(9):
        linha = [' ']+list(range(1,9))
        peso = [20]+([1]*8)
        #print('Pe',peso)
        matrix.append(random.choices(linha, weights=peso,k=9))
        #matrix.append([" "]*9)
    # matrix = [[9, 8, 7, ' ', 3, 2, 6, 5, 4], [6, 5, 4, 9, 8, 7, ' ', 3, 2], [' ', 3, 2, 6, 5, 4, 9, 8, 7], [7, 9, 8, 2, ' ', 3, 4, 6, 5], [4, 6, 5, 7, 9, 8, 2, ' ', 3], [2, ' ', 3, 4, 6, 5, 7, 9, 8], [8, 7, 9, 3, 2, ' ', 5, 4, 6], [5, 4, 6, 8, 7, 9, 3, ' ', ' '], [3, 2, ' ', 5, 4, 6, 8, 7, 9]]
    return matrix

def mostrarTabuleiro(matrix):
    '''Mostra o tabuleiro de uma maneira agradável.'''
    for linha in matrix:
        for item in linha:
            print(item, '', end= '')
        print()
        # print()

def girar(matrix):
    '''Faz as colunas virarem linhas para que possam ser verificadas como tal.'''
    matrixColunas = []
    for indice in range(len(matrix)):
        coluna = []
        for linha in matrix:
            coluna.append(linha[indice])
        matrixColunas.append(coluna)
    return matrixColunas

def celula(n): # How delightful! And Scary!
    '''Retorna uma lista com as cordenadas de cada valor da célula.'''
    celula = []
    x = n % 3
    y = n // 3
    for linha in range(y*3, y*3+3):
        for item in range(x*3, x*3+3):
            celula.append([linha, item])
    return celula

def verificar(matrix): # Dligthful but scary!
    '''Verifica e retorna uma lista com todas as cordenadas dos valores em conflito.'''
    conflitos = []
    for vez in range(2):

        for l, linha in enumerate(matrix):
            for valor in linha:
                if valor != ' ' and linha.count(valor) > 1:
                    for i, item in enumerate(linha):
                        if item == valor:
                            match vez:
                                case 0:
                                    if [l,i] not in conflitos:
                                        conflitos.append([l,i])
                                case 1:
                                    if [i,l] not in conflitos:
                                        conflitos.append([i,l])
        matrix = girar(matrix)

    for p in range(9):
        cell = celula(p)
        cellVal = []
        for i in cell:
            cellVal.append(matrix[i[0]][i[1]])
        for i, val in enumerate(cellVal):
            if cellVal.count(val) > 1 and cell[i] not in conflitos and val != ' ':
                coord = cell[i]
                conflitos.append([coord[0],coord[1]])

    # Verificar Vitória
    completo = True
    for i in matrix:
        if ' ' in i:
            completo = False
            break
    if (len(conflitos) == 0) and completo:
        print('Você ganhou o Sudoku!\nModo Sandbox')

    # Debug
    print(conflitos)
    print(len(conflitos))
    
    return conflitos

def mostrarConflitos(matrix, conflitos):
    '''Percorre a lista de cordenadas dos valores errados e os colore.'''
    for l in range(9):
        for i in range(9):
            if (l, i) in conflitos or [l, i] in conflitos:
                tabuleiroBotoes[l][i].config(foreground="#ff0a0a")
            else:
                tabuleiroBotoes[l][i].config(foreground="#000000")

# def limpar(lista):
#     '''Remove quaisquer itens repetidos.'''
#     nLista = []
#     for i in lista:
#         if not i in nLista:
#             nLista.append(i)
#     return nLista

def inserir(linha, coluna):
    tabuleiroBotoes[linha][coluna].config(text=numeroSelecionado)
    tabuleiro[linha][coluna] = numeroSelecionado
    mostrarTabuleiro(tabuleiro)
    mostrarConflitos(tabuleiro, verificar(tabuleiro))

def selecionarNumero(linha):
    global numeroSelecionado
    numeroSelecionado = linha if linha != 0 else ' '
    print(numeroSelecionado)

def Ui():
    '''Gera a interface'''
    global tabuleiroBotoes
    tabuleiroBotoes = []
    for i in range(9):
        tabuleiroBotoesLinha = []
        for j in range(9):
            botao = tk.Button(root,bg='#99ccff', activebackground='#6699ff',height=2,width=2, text=tabuleiro[i][j], command=lambda linha=i, coluna=j:inserir(linha,coluna))
            botao.grid(row=i, column=j)
            tabuleiroBotoesLinha.append(botao)
        tabuleiroBotoes.append(tabuleiroBotoesLinha)
        
    for i in range(10):
        algarismos = []
        algarismo = tk.Button(root, bg="#3bffde", activebackground="#3be2ff", height=2, width=4,text=i if i != 0 else '', command=lambda linha=i: selecionarNumero(linha))
        algarismo.grid(row=i,column=10)
        algarismos.append(algarismo)

def iniciar():
    global tabuleiro, root, numeroSelecionado
    print('-'*30)
    tabuleiro = gerar()
    numeroSelecionado = ''
    print(tabuleiro)
    #mostrarTabuleiro(tabuleiro)
    root = tk.Tk()
    root.title('Python Sudoku v1')
    root.config(background='#305f6f')#RRGGBB
    root.geometry('500x500')
    Ui()
    mostrarConflitos(tabuleiro, verificar(tabuleiro))

    root.mainloop()

    print('-'*30)

if __name__ == '__main__':
    print('In Main script!')
    iniciar()