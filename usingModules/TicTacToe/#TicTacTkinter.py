#From text to GUI
from tkinter import *
root = Tk()
root.title('Jogo Da Velha')
root.config(background='#305f6f')#RRGGBB
root.geometry('400x400')
l1 = 0
l2 = 0
l3 = 0
l4 = 0
l5 = 0
l6 = 0
l7 = 0
l8 = 0
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
b11 = Button(root,bg='#99ccff', activebackground='#6699ff',height=5,width=10)
b12 = Button(root,bg='#99ccff', activebackground='#6699ff',height=5,width=10)
b13 = Button(root,bg='#99ccff', activebackground='#6699ff',height=5,width=10)
b21 = Button(root,bg='#99ccff', activebackground='#6699ff',height=5,width=10)
b22 = Button(root,bg='#99ccff', activebackground='#6699ff',height=5,width=10)
b23 = Button(root,bg='#99ccff', activebackground='#6699ff',height=5,width=10)
b31 = Button(root,bg='#99ccff', activebackground='#6699ff',height=5,width=10)
b32 = Button(root,bg='#99ccff', activebackground='#6699ff',height=5,width=10)
b33 = Button(root,bg='#99ccff', activebackground='#6699ff',height=5,width=10)
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
    global l1, l2, l3, l4, l5, l6, l7, l8, local, ocupados, lugares
    global pontosx, pontoso, empates, jogador
    print(ocupados)
    #while ocupados != []: #Quando apertar um botão
    try:
        l = str(local)
        ocupados.pop(ocupados.index(l))
        l = int(l)
        lugares[l - 1] = xo()
        print(xo())
    except Exception as e:
        #print(e)
        pass
    else:
        match l:
            case 1:
                if xo() == imagemx:
                    l1 += 1
                    l4 += 1
                    l7 += 1
                else:
                    l1 -= 1
                    l4 -= 1
                    l7 -= 1
            case 2:
                if xo() == imagemx:
                    l1 += 1
                    l5 += 1
                else:
                    l1 -= 1
                    l5 -= 1
            case 3:
                if xo() == imagemx:
                    l1 += 1
                    l6 += 1
                    l8 += 1#
                else:
                    l1 -= 1
                    l6 -= 1
                    l8 -= 1#
            case 4:
                if xo() == imagemx:
                    l2 += 1
                    l4 += 1
                else:
                    l2 -= 1
                    l4 -= 1
            case 5:
                if xo() == imagemx:
                    l2 += 1
                    l5 += 1
                    l7 += 1
                    l8 += 1
                else:
                    l2 -= 1
                    l5 -= 1
                    l7 -= 1
                    l8 -= 1
            case 6:
                if xo() == imagemx:
                    l2 += 1
                    l6 += 1
                else:
                    l2 -= 1
                    l6 -= 1
            case 7:
                if xo() == imagemx:
                    l3 += 1
                    l4 += 1
                    l8 += 1
                else:
                    l3 -= 1
                    l4 -= 1
                    l8 -= 1
            case 8:
                if xo() == imagemx:
                    l3 += 1
                    l5 += 1
                else:
                    l3 -= 1
                    l5 -= 1
            case 9:
                if xo() == imagemx:
                    l3 += 1
                    l6 += 1
                    l7 += 1
                else:
                    l3 -= 1
                    l6 -= 1
                    l7 -= 1
        #tabuleiro()
        if l1 == 3 or l2 == 3 or l3 == 3 or l4 == 3 or l5 == 3 or l6 == 3 or l7 == 3 or l8 == 3:
            print("X Ganhou!")
            pontosx += 1
            lblx.config(text=f'X: {pontosx}')   
            disableAll()
        elif l1 == -3 or l2 == -3 or l3 == -3 or l4 == -3 or l5 == -3 or l6 == -3 or l7 == -3 or l8 == -3:
            print("O Ganhou!")
            pontoso += 1
            lblo.config(text=f'O: {pontoso}')
            disableAll()
        elif ocupados == []:
            print("Deu velha! (Empate!)")
            empates += 1
            lble.config(text=f'Empates: {empates}')
            disableAll()
        if l1 == 3 or l1 == -3:
            b11.config(bg='#ffcc66')
            b12.config(bg='#ffcc66')
            b13.config(bg='#ffcc66')
        if l2 == 3 or l2 == -3:
            b21.config(bg='#ffcc66')
            b22.config(bg='#ffcc66')
            b23.config(bg='#ffcc66')
        if l3 == 3 or l3 == -3:
            b31.config(bg='#ffcc66')
            b32.config(bg='#ffcc66')
            b33.config(bg='#ffcc66')
        if l4 == 3 or l4 == -3:
            b11.config(bg='#ffcc66')
            b21.config(bg='#ffcc66')
            b31.config(bg='#ffcc66')
        if l5 == 3 or l5 == -3:
            b12.config(bg='#ffcc66')
            b22.config(bg='#ffcc66')
            b32.config(bg='#ffcc66')
        if l6 == 3 or l6 == -3:
            b13.config(bg='#ffcc66')
            b23.config(bg='#ffcc66')
            b33.config(bg='#ffcc66')
        if l7 == 3 or l7 == -3:
            b11.config(bg='#ffcc66')
            b22.config(bg='#ffcc66')
            b33.config(bg='#ffcc66')
        if l8 == 3 or l8 == -3:
            b13.config(bg='#ffcc66')
            b22.config(bg='#ffcc66')
            b31.config(bg='#ffcc66')
        print(f"l1:{l1} | l2:{l2} | l3:{l3} | l4:{l4} | l5:{l5} | l6:{l6} | l7:{l7} | l8:{l8}")#Debug
        MudarJogador()

def click1():
    global local
    local = 1
    b11.config(image=xo(),height=83,width=92, state=DISABLED)
    run()
def click2():
    global local
    local = 2
    b12.config(image=xo(),height=83,width=92, state=DISABLED)
    run()
def click3():
    global local
    local = 3
    b13.config(image=xo(),height=83,width=92, state=DISABLED)
    run()
def click4():
    global local
    local = 4
    b21.config(image=xo(),height=83,width=92, state=DISABLED)
    run()
def click5():
    global local
    local = 5
    b22.config(image=xo(),height=83,width=92, state=DISABLED)
    run()
def click6():
    global local
    local = 6
    b23.config(image=xo(),height=83,width=92, state=DISABLED)
    run()
def click7():
    global local
    local = 7
    b31.config(image=xo(),height=83,width=92, state=DISABLED)
    run()
def click8():
    global local
    local = 8
    b32.config(image=xo(),height=83,width=92, state=DISABLED)
    run()
def click9():
    global local
    local = 9
    b33.config(image=xo(),height=83,width=92, state=DISABLED)
    run()

def disableAll():
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)
    b13.config(state=DISABLED)
    b21.config(state=DISABLED)
    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)
def enableAll():
    global l1, l2, l3, l4, l5, l6, l7, l8, ocupados, lugares, jogador, pontoso, pontosx
    l1 = l2 = l3 = l4 = l5 = l6 = l7 = l8 = 0
    ocupados = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    lugares = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    jogador = 1
    b11.config(image='',bg='#99ccff',state=ACTIVE,height=5,width=10)
    b12.config(image='',bg='#99ccff',state=ACTIVE,height=5,width=10)
    b13.config(image='',bg='#99ccff',state=ACTIVE,height=5,width=10)
    b21.config(image='',bg='#99ccff',state=ACTIVE,height=5,width=10)
    b22.config(image='',bg='#99ccff',state=ACTIVE,height=5,width=10)
    b23.config(image='',bg='#99ccff',state=ACTIVE,height=5,width=10)
    b31.config(image='',bg='#99ccff',state=ACTIVE,height=5,width=10)
    b32.config(image='',bg='#99ccff',state=ACTIVE,height=5,width=10)
    b33.config(image='',bg='#99ccff',state=ACTIVE,height=5,width=10)

reset = Button(root,font=('mono',30,'bold'),text='New round',command=enableAll).grid(row=5,column=1)
#titulo = Label(font=('arial',20,'bold'),text='Jogo da Velha').pack(x=0,y=0)
b11.config(command=click1)
b12.config(command=click2)
b13.config(command=click3)
b21.config(command=click4)
b22.config(command=click5)
b23.config(command=click6)
b31.config(command=click7)
b32.config(command=click8)
b33.config(command=click9)

b11.grid(row=1,column=0)
b12.grid(row=1,column=1)
b13.grid(row=1,column=2)
b21.grid(row=2,column=0)
b22.grid(row=2,column=1)
b23.grid(row=2,column=2)
b31.grid(row=3,column=0)
b32.grid(row=3,column=1)
b33.grid(row=3,column=2)
lblx.grid(row=4,column=0)
lblo.grid(row=4,column=1)
lble.grid(row=4,column=2)
root.mainloop()