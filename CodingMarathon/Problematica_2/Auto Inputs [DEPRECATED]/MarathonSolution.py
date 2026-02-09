# Estoque

""" Estoque == Tabela
  1 2 3 - Tamanho
1 # # #
2 # # #
3 # # #
4 # # #

# = número de peças no estoque
"""

# Uma peça de roupa é vendida()
 # Atualizar o estoque
 # Apenas se ela estiver disponível

inputs = """4 3
5 2 2
6 4 0
2 1 4
1 3 2
2
1 1
2 3
1 4
1 3 2 5
4
1 3
1 3
1 3
1 4
0 0
"""
from Inputs import AutoInputs
auto = AutoInputs(True)

def getInput():
    return auto.input(inputs)
    
# def getInput():
    # return list(map(int, input().split()))

# Quantas peças foram vendidas no total?
def gerenciarEstoque():
    msg = ("GERANDO", "OBTENDO", "INPUT", "OUTPUT")
    
    def obterEstoque(tipos, tamanhos):
        estoque = []
        for i in range(tipos):
            print(msg[1])
            estoque.append(getInput())
        print(estoque)
        return estoque

    while True:
        TIPOS, TAMANHOS = getInput()
        if TIPOS == TAMANHOS == 0:
            return
        print(msg[0])
        ESTOQUE = obterEstoque(TIPOS, TAMANHOS)

        # Pedidos
        P = getInput()[0]
        vendidas = 0
        for i in range(P):
            tipo, tamanho = getInput()
            tipo -= 1
            tamanho -= 1
            if ESTOQUE[tipo][tamanho] != 0:
                ESTOQUE[tipo][tamanho] -= 1
                vendidas += 1
                print(ESTOQUE)
        print(msg[3], vendidas)

gerenciarEstoque()
"""Notas
Usar array dentro de array [i][j] em vez de classes
Usar NumPy
"""

