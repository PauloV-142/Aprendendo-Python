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
jogador = 1
while ocupados != []:
    try:
        l = local()
        lugares[l - 1] = xo()
        MudarJogador()
        l = str(l)
        ocupados.pop(ocupados.index(l))
    except Exception as e:
        print(e)
print(lugares)