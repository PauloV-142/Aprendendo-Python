#From text to GUI
from tkinter import *
root = Tk()
root.title('Jogo Da Velha')
root.config(background='#305f6f')#RRGGBB
root.geometry('400x400')
soma = [0]*8
imagemx = ''
imagemo = ''
lugares = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
ocupados = lugares.copy()
jogador = 1
pontuacao = [0]*3
imagemx = PhotoImage(file='/sysroot/home/user/Documentos/Programaçao/VSCode Python/usingModules/TicTacToe/icons8-cross-90.png')
imagemo = PhotoImage(file='/sysroot/home/user/Documentos/Programaçao/VSCode Python/usingModules/TicTacToe/icons8-circle-64.png')
#botões
b = ['']*9
for i in range(9):
    b[i] = Button(root,bg='#99ccff', activebackground='#6699ff',height=5,width=10)

lblx = Label(font=('mono',50,'bold'),text='X: 0',bg='#305f6f',fg='white')
lblo = Label(font=('mono',50,'bold'),text='O: 0',bg='#305f6f',fg='white')
lble = Label(font=('mono',50,'bold'),text='Empates: 0',bg='#305f6f',fg='white')

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

def run():
    global soma, local, ocupados, lugares, pontuacao, jogador, b
    try: #Try Except pode ser removido, foi para debug.
        l = str(local+1)
        ocupados.pop(ocupados.index(l))
        l = int(l)-1
        lugares[l] = xo()
        # print(xo())
    except Exception as e:
        print(e)
        pass
    else:
        #Cordenadas a serem alteradas NA LISTA DE SOMAS. #A soma é feita com base nas possíveis LINHAS A SEREM FORMADAS, e não nos LUGARES.
        tabSoma = ({0,3,6},{0,5},{0,5,7},{1,3},{1,4,6,7},{2,5},{2,3,7},{2,4},{2,5,6})#Posso usar o tipo de array mais rápido aqui (set), no lugar das listas :D #E nem precisa do dicionário.
        for i in tabSoma[l]:
            if xo() == imagemx:
                soma[i] += 1
            else:
                soma[i] -= 1

        # #tabuleiro()
        #Verificar vitória
        for s in soma:
            if s == 3:
                print("X Ganhou!")
                pontuacao[0] += 1
                lblx.config(text=f'X: {pontuacao[0]}')
                disableAll()
                break
            elif s == -3:
                print("O Ganhou!")
                pontuacao[1] += 1
                lblo.config(text=f'O: {pontuacao[1]}')
                disableAll()
                break
            elif ocupados == []:
                print("Deu velha! (Empate!)")
                pontuacao[2] += 1
                lble.config(text=f'Empates: {pontuacao[2]}')
                disableAll()
                break
        
        #Colorir os quadrados vencedores.
        bColorir = ({0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}) #Tupla com as cordenadas dos possíveis quadrados vencedores.
        for i in range(8):
            if soma[i] == 3 or soma[i] == -3: #soma[i] == (3 or -3) ??
                for c in bColorir[i]:
                    b[c].config(bg='#ffcc66')
        # print(f"l1:{soma[0]} | l2:{soma[1]} | l3:{soma[2]} | l4:{soma[3]} | l5:{soma[4]} | l6:{soma[5]} | l7:{soma[6]} | l8:{soma[7]}")# Debug
        MudarJogador()

def disableAll():
    global b
    for i in range(9):
        b[i].config(state=DISABLED)


def enableAll():
    global soma, ocupados, lugares, jogador, pontuacao, b
    soma = [0] * 8                                                    ######
    ocupados = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    lugares = ocupados.copy()
    jogador = (sum(pontuacao)%2)+1
    for i in range(9):
        b[i].config(image='',bg='#99ccff',state=ACTIVE,height=5,width=10)

def click(linha,coluna):
    global local, b
    # print(linha, coluna)
    local = linha*3+coluna
    b[local].config(image=xo(),height=83,width=92, state=DISABLED)
    run()

reset = Button(root,font=('mono',30,'bold'),text='New round',command=enableAll).grid(row=5,column=1)
#titulo = Label(font=('arial',20,'bold'),text='Jogo da Velha').pack(x=0,y=0)
for i in range(3):
    for j in range(3):
        b[i*3+j].config(command= lambda linha=i, coluna=j:click(linha,coluna))

for i in range(3):
    for j in range(3):
        b[i*3+j].grid(row=i+1,column=j)

lblx.grid(row=4,column=0)
lblo.grid(row=4,column=1)
lble.grid(row=4,column=2)
root.mainloop()

##Adicionar uma Rede Neural futuramente.