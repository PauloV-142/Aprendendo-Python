#From text to GUI
from tkinter import *
root = Tk()
root.title('Jogo Da Velha')
root.config(background='#305f6f')#RRGGBB
root.geometry('400x400')

imagemx = ''
imagemo = ''
imagemx = PhotoImage(file='/sysroot/home/user/Documentos/Programaçao/VSCode Python/usingModules/TicTacToe/icons8-cross-90.png')
imagemo = PhotoImage(file='/sysroot/home/user/Documentos/Programaçao/VSCode Python/usingModules/TicTacToe/icons8-circle-64.png')

pontuacao = [0]*3

lblx = Label(font=('mono',50,'bold'),text='X: 0',bg='#305f6f',fg='white')
lblo = Label(font=('mono',50,'bold'),text='O: 0',bg='#305f6f',fg='white')
lble = Label(font=('mono',50,'bold'),text='Empates: 0',bg='#305f6f',fg='white')

#Células como botões
def criar_botao(linha, coluna):
    return lambda: click(linha, coluna)
b = []
for i in range(3):
    for j in range(3):
        b.append(Button(root, bg='#99ccff', activebackground='#6699ff', height=5, width=10, command=criar_botao(i,j)))

def novoJogo():
    global soma, ocupados, lugares, jogador, pontuacao, b, tabuleiro
    soma = [0]*8
    ocupados = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    lugares = ocupados.copy()
    jogador = (sum(pontuacao)%2)+1
    tabuleiro = [0]*9
    for i in b:
        i.config(image='',bg='#99ccff',state=ACTIVE,height=5,width=10)

def fimDeJogo():
    global b
    for i in range(9):
        b[i].config(state=DISABLED)


def MudarJogador(): # Alterna entre 1 ou 2
    global jogador
    if jogador == 1:
        jogador = 2
    else:
        jogador = 1

def xo(): # X ou O dependendo do jogador.
    global jogador
    if jogador == 1:
        return imagemx
    else:
        return imagemo

def click(linha,coluna):
    global local, b
    # print(linha, coluna)
    local = linha*3+coluna
    b[local].config(image=xo(),height=83,width=92, state=DISABLED)
    run()
    
def run():
    global soma, local, ocupados, lugares, pontuacao, jogador, b
    l = str(local+1)
    ocupados.pop(ocupados.index(l))
    l = int(l)-1
    lugares[l] = xo()
    # print(xo())
    if jogador == 1:
        tabuleiro[local] += 1
    else:
        tabuleiro[local] -= 1

    #Verificar vitória
    linhas = ({0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}) #Talvez seja mais fácil com o numpy, se tiver a opção de colunas em matrizes.
    for linha in linhas:
        soma = 0
        for c in linha:
            soma += tabuleiro[c]
        if soma == 3:
            print("X Ganhou!")
            pontuacao[0] += 1
            lblx.config(text=f'X: {pontuacao[0]}')
            colorir(linha)
            fimDeJogo()
            break
        elif soma == -3:
            print("O Ganhou!")
            pontuacao[1] += 1
            lblo.config(text=f'O: {pontuacao[1]}')
            colorir(linha)
            fimDeJogo()
            break
        elif ocupados == []:
            print("Deu velha! (Empate!)")
            pontuacao[2] += 1
            lble.config(text=f'Empates: {pontuacao[2]}')
            break
    MudarJogador()

def colorir(linha):
    global b
    for i in linha:
        b[i].config(bg='#ffcc66')

novoJogo()

#Fazer tudo aparecer na tela
reset = Button(root,font=('mono',30,'bold'),text='New round',command=novoJogo).grid(row=5,column=1)
titulo = Label(font=('arial',10),text='Jogo da Velha', bg='#305f6f', fg='white').grid(row=0,column=1)

for ib, botao in enumerate(b):
    i = (ib%3)
    j = ib//3
    botao.grid(row=i,column=j)

#Labels Pontuação
lblx.grid(row=4,column=0)
lblo.grid(row=4,column=1)
lble.grid(row=4,column=2)
root.mainloop()

#Adicionar uma Rede Neural futuramente.