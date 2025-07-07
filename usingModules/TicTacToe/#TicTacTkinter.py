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
ocupados = lugares[:]
jogador = 1
pontosx = 0
pontoso = 0
empates = 0
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
    global soma, local, ocupados, lugares, pontosx, pontoso, empates, jogador, b
    # print(ocupados)
    #while ocupados != []: #Quando apertar um botão
    try:
        l = str(local)
        ocupados.pop(ocupados.index(l))
        l = int(l)
        lugares[l - 1] = xo()
        print(xo())
    except Exception as e:
        print(e)
        pass
    else:
        match l:
            case 1:
                if xo() == imagemx:             ######             ######
                    soma[0] += 1
                    soma[3] += 1
                    soma[6] += 1
                else:
                    soma[0] -= 1
                    soma[3] -= 1
                    soma[6] -= 1
            case 2:
                if xo() == imagemx:
                    soma[0] += 1
                    soma[5] += 1
                else:
                    soma[0] -= 1
                    soma[5] -= 1
            case 3:
                if xo() == imagemx:
                    soma[0] += 1
                    soma[5] += 1
                    soma[7] += 1
                else:
                    soma[0] -= 1
                    soma[5] -= 1
                    soma[7] -= 1
            case 4:
                if xo() == imagemx:
                    soma[1] += 1
                    soma[3] += 1
                else:
                    soma[1] -= 1
                    soma[3] -= 1
            case 5:
                if xo() == imagemx:
                    soma[1] += 1
                    soma[4] += 1
                    soma[6] += 1
                    soma[7] += 1
                else:
                    soma[1] -= 1
                    soma[4] -= 1
                    soma[6] -= 1
                    soma[7] -= 1
            case 6:
                if xo() == imagemx:
                    soma[2] += 1
                    soma[5] += 1
                else:
                    soma[2] -= 1
                    soma[5] -= 1
            case 7:
                if xo() == imagemx:
                    soma[2] += 1
                    soma[3] += 1
                    soma[7] += 1
                else:
                    soma[2] -= 1
                    soma[3] -= 1
                    soma[7] -= 1
            case 8:
                if xo() == imagemx:
                    soma[2] += 1
                    soma[4] += 1
                else:
                    soma[2] -= 1
                    soma[4] -= 1
            case 9:
                if xo() == imagemx:
                    soma[2] += 1
                    soma[5] += 1
                    soma[6] += 1
                else:
                    soma[2] -= 1
                    soma[5] -= 1
                    soma[6] -= 1
        #tabuleiro()
        for s in soma:
            if s == 3:             ######
                print("X Ganhou!")
                pontosx += 1
                lblx.config(text=f'X: {pontosx}')   
                disableAll()
                break
            elif s == -3:             ######
                print("O Ganhou!")
                pontoso += 1
                lblo.config(text=f'O: {pontoso}')
                disableAll()
                break
            elif ocupados == []:
                print("Deu velha! (Empate!)")
                empates += 1
                lble.config(text=f'Empates: {empates}')
                disableAll()
                break
        if soma[0] == 3 or soma[0] == -3:
            b[0].config(bg='#ffcc66')
            b[1].config(bg='#ffcc66')
            b[2].config(bg='#ffcc66')
        if soma[1] == 3 or soma[1] == -3:
            b[3].config(bg='#ffcc66')
            b[4].config(bg='#ffcc66')
            b[5].config(bg='#ffcc66')
        if soma[2] == 3 or soma[2] == -3:
            b[6].config(bg='#ffcc66')
            b[7].config(bg='#ffcc66')
            b[8].config(bg='#ffcc66')
        if soma[3] == 3 or soma[3] == -3:
            b[0].config(bg='#ffcc66')
            b[3].config(bg='#ffcc66')
            b[6].config(bg='#ffcc66')
        if soma[4] == 3 or soma[4] == -3:
            b[1].config(bg='#ffcc66')
            b[4].config(bg='#ffcc66')
            b[7].config(bg='#ffcc66')
        if soma[5] == 3 or soma[5] == -3:
            b[2].config(bg='#ffcc66')
            b[5].config(bg='#ffcc66')
            b[8].config(bg='#ffcc66')
        if soma[6] == 3 or soma[6] == -3:
            b[0].config(bg='#ffcc66')
            b[4].config(bg='#ffcc66')
            b[8].config(bg='#ffcc66')
        if soma[7] == 3 or soma[7] == -3:
            b[2].config(bg='#ffcc66')
            b[4].config(bg='#ffcc66')
            b[6].config(bg='#ffcc66')
        # print(f"l1:{soma[0]} | l2:{soma[1]} | l3:{soma[2]} | l4:{soma[3]} | l5:{soma[4]} | l6:{soma[5]} | l7:{soma[6]} | l8:{soma[7]}")# Debug
        MudarJogador()
        print('jogadorMudou')


def disableAll():
    global b
    for i in range(9):
        b[i].config(state=DISABLED)


def enableAll():
    global soma, ocupados, lugares, jogador, pontoso, pontosx, b
    soma = [0] * 8                                                    ######
    ocupados = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    lugares = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    jogador = 1
    for i in range(9):
        b[i].config(image='',bg='#99ccff',state=ACTIVE,height=5,width=10)

def click(linha,coluna):
    global local, b
    print(linha, coluna)
    local = linha*3+coluna+1
    b[local-1].config(image=xo(),height=83,width=92, state=DISABLED)
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