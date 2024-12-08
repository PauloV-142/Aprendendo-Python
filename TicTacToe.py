l1 = 0
l2 = 0
l3 = 0
l4 = 0
l5 = 0
l6 = 0
l7 = 0
l8 = 0

lugares = ["N", "N", "N", "N", "N", "N", "N", "N", "N"]
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
while ocupados != []:
    try:
        l = str(local())
        ocupados.pop(ocupados.index(l))
        l = int(l)
        lugares[l - 1] = xo()
    except Exception as e:
        print(e)
    else:
        MudarJogador()
        tabuleiro()