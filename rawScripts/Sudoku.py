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

def mostrarTabuleiro(matrix):
    '''Mostra o tabuleiro de uma maneira agradável.'''
    for linha in matrix:
        for item in linha:
            print(item, ' ', end= ' ')
        print()
        print()


def verificar(matrix): #Entenda se conseguir
    '''Verifica e retorna uma lista com todas as cordenadas dos valores errados.'''
    erros = []
    for linha in matrix:
        for i in range(9):
            if linha[i] in range(1,9):
                if linha.count(linha[i]) > 1:
                    erros.append([matrix.index(linha),i])
    return erros

def girar(matrix):
    '''Faz as colunas virarem linhas para que possam ser verificadas como tal.'''
    matrixColunas = []
    for indice in range(9):
        coluna = []
        for linha in matrix:
            coluna.append(linha[indice])
        matrixColunas.append(coluna)
    return matrixColunas

def mostrarErros(matrix, erros):
    '''Percorre a lista de cordenadas dos valores errados e os colore de verde.'''
    for item in erros:
        matrix[item[0]][item[1]] = f"\033[32m{matrix[item[0]][item[1]]}\033[0m"
    return matrix

def limpar(lista):
    nLista = []
    for i in lista:
        if not i in nLista:
            nLista.append(i)
    return nLista

def inserir(linha, coluna):
    tabuleiroBotoes[linha][coluna].config(text=numeroSelecionado)
    tabuleiro[linha][coluna] = numeroSelecionado
    mostrarTabuleiro(tabuleiro)

def selecionarNumero(linha):
    global numeroSelecionado
    numeroSelecionado = linha
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
        
    for i in range(9):
        algarismos = []
        algarismo = tk.Button(root, bg="#3bffde", activebackground="#3be2ff", height=2, width=4,text=i+1, command=lambda linha=i+1: selecionarNumero(linha))
        algarismo.grid(row=i,column=10)
        algarismos.append(algarismo)

numeroSelecionado = ''

tabuleiro = gerar()
mostrarTabuleiro(tabuleiro)

root = tk.Tk()
root.title('Python Sudoku v1')
root.config(background='#305f6f')#RRGGBB
root.geometry('500x500')
Ui()


        
root.mainloop()

print('-'*30)