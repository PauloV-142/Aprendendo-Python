'''Work In Progress...'''
print('\033[0m-'*30)
import random
import tkinter as tk

def gerar():
    '''Gera todo o tabuleiro com números aleatórios, por enquanto.'''
    matrix = []
    for i in range(9):
        #linha = list(range(1,9))
        #matrix.append(random.choices(linha, k=9))
        matrix.append([""]*9)
    return matrix
tabuleiro = gerar()

def mostrarTabuleiro(matrix):
    '''Mostra o tabuleiro de uma maneira agradável.'''
    for linha in matrix:
        for item in linha:
            print(item, ' ', end= ' ')
        print()
        print()

def girar(matrix):
    '''Faz as colunas virarem linhas para que possam ser verificadas como tal.'''
    matrixColunas = []
    for indice in range(len(matrix)):
        coluna = []
        for linha in matrix:
            coluna.append(linha[indice])
        matrixColunas.append(coluna)
    return matrixColunas

def verificarLinha(matrix):
    '''Verifica e retorna uma lista com todas as cordenadas dos valores em conflito.'''
    conflitos = []
    for vez in range(2):
        for l, linha in enumerate(matrix):
            for valor in linha:
                if valor != '' and linha.count(valor) > 1:
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

    return conflitos

def verificarTudo(matrix):
    '''Aplica o método de verificar linha, coluna e célula e retorna os lugares com erro.'''
    erros = verificarLinha(matrix)
    print(len(erros))
    erros = limpar(erros)
    print(len(erros))
    return erros

def mostrarConflitos(matrix, conflitos):
    '''Percorre a lista de cordenadas dos valores errados e os colore.'''
    for l in range(9):
        for i in range(9):
            if (l, i) in conflitos or [l, i] in conflitos:
                tabuleiroBotoes[l][i].config(foreground="#ff0a0a")
            else:
                tabuleiroBotoes[l][i].config(foreground="#000000")
def limpar(lista):
    '''Remove quaisquer itens repetidos.'''
    nLista = []
    for i in lista:
        if not i in nLista:
            nLista.append(i)
    return nLista

def inserir(linha, coluna):
    tabuleiroBotoes[linha][coluna].config(text=numeroSelecionado)
    tabuleiro[linha][coluna] = numeroSelecionado
    mostrarTabuleiro(tabuleiro)
    mostrarConflitos(tabuleiro, verificarTudo(tabuleiro))

def selecionarNumero(linha):
    global numeroSelecionado
    numeroSelecionado = linha if linha != 0 else ''
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

numeroSelecionado = ''
mostrarTabuleiro(tabuleiro)
root = tk.Tk()
root.title('Python Sudoku v1')
root.config(background='#305f6f')#RRGGBB
root.geometry('500x500')
Ui()

root.mainloop()

print('-'*30)