l1 = 0
l2 = 0
l3 = 0
l4 = 0
l5 = 0
l6 = 0
l7 = 0
l8 = 0

lugares = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
ocupados = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
jogador = 1
def MudarJogador(): # Alterna entre X ou O
    global jogador
    if jogador == 1:
        jogador = 2
    else:
        jogador = 1
    
def xo(): # X ou O dependendo do jogador.
    global jogador
    if jogador == 1:
        return "X"
    else:
        return "O"
def local():
    local = int(input(f"Digite um número ({ocupados}): "))
    return local
def tabuleiro():
    print(f"{lugares[0]} | {lugares[1]} | {lugares[2]}\n-- --- --\n{lugares[3]} | {lugares[4]} | {lugares[5]}\n-- --- --\n{lugares[6]} | {lugares[7]} | {lugares[8]}")
tabuleiro()
while ocupados != []:
    try:
        l = str(local())
        ocupados.pop(ocupados.index(l))
        l = int(l)
        lugares[l - 1] = xo()
    except Exception as e:
        print(e)
    else:
        match l:
            case 1:
                if xo() == "X":
                    l1 += 1
                    l4 += 1
                    l7 += 1
                else:
                    l1 -= 1
                    l4 -= 1
                    l7 -= 1
            case 2:
                if xo() == "X":
                    l1 += 1
                    l5 += 1
                else:
                    l1 -= 1
                    l5 -= 1
            case 3:
                if xo() == "X":
                    l1 += 1
                    l6 += 1
                    l8 += 1#
                else:
                    l1 -= 1
                    l6 -= 1
                    l8 -= 1#
            case 4:
                if xo() == "X":
                    l2 += 1
                    l4 += 1
                else:
                    l2 -= 1
                    l4 -= 1
            case 5:
                if xo() == "X":
                    l2 += 1
                    l5 += 1
                    l7 += 1
                else:
                    l2 -= 1
                    l5 -= 1
                    l7 -= 1
            case 6:
                if xo() == "X":
                    l2 += 1
                    l6 += 1
                else:
                    l2 -= 1
                    l6 -= 1
            case 7:
                if xo() == "X":
                    l3 += 1
                    l4 += 1
                    l8 += 1
                else:
                    l3 -= 1
                    l4 -= 1
                    l8 -= 1
            case 8:
                if xo() == "X":
                    l3 += 1
                    l5 += 1
                else:
                    l3 -= 1
                    l5 -= 1
            case 9:
                if xo() == "X":
                    l3 += 1
                    l6 += 1
                    l7 += 1
                else:
                    l3 -= 1
                    l6 -= 1
                    l7 -= 1
        tabuleiro()
        if l1 == 3 or l2 == 3 or l3 == 3 or l4 == 3 or l5 == 3 or l6 == 3 or l7 == 3 or l8 == 3:
            print("X Ganhou!")
            exit()
        elif l1 == -3 or l2 == -3 or l3 == -3 or l4 == -3 or l5 == -3 or l6 == -3 or l7 == -3 or l8 == -3:
            print("O Ganhou!")
            exit()
        print(f"l1:{l1} | l2:{l2} | l3:{l3} | l4:{l4} | l5:{l5} | l6:{l6} | l7:{l7} | l8:{l8}")
        MudarJogador()# 2 3 5 7 1