inputs = """
8
ADM001 A 125.5
DEV001 D 89.3
DEV002 D 156.7
PROD01 P 245.8
ADM001 A 98.2
VEN001 V 67.4
DEV001 D 201.1
MAN001 M 178.9
"""

from inputs import gen_inputs
from pprint import pprint
gen = gen_inputs(inputs)
def getInput():
    """Acess the next output from a generator."""
    try:
        print("AUTO:", nx := next(gen), sep="\t")
        return nx
    except StopIteration:
        print("\t\t!Automatic inputs just ran out!")
    return input()

def count(n):
    for i in range(n+1):
        yield i
counter = count(9)

class Tipo:
    departamentos = dict()
    medias_tipos = dict()
    
    def __init__(self, tipo):
        self.tipo = tipo
        if not tipo in Tipo.medias_tipos.keys():
            Tipo.departamentos[tipo] = []
            Tipo.medias_tipos[tipo] = 0

    def calcMediasTipos(self, qtde):
        # Not work for loops
        # for cod, array in Tipo.departamentos:
        #     for obj in array:
        #         Tipo.medias_tipos[cod] += obj.media_departamento
        Tipo.medias_tipos[self.tipo] += self.media_departamento / qtde
            

    def __str__(self):
        return f"{self.tipo} medias_tipos:{self.medias_tipos}"

class Departamento(Tipo):
    def __init__(self, cod, tipo, consumo):
        self.cod = cod
        super().__init__(tipo)
        self.consumo = [consumo]
        self.media_departamento = 0

    def calcMediaDepartamento(self):
        self.media_departamento = sum(self.consumo) / len(self.consumo)

    def __str__(self):
        return f"{self.cod} {self.tipo} {self.consumo} media:{self.media_departamento}"


def energia():
    while True:
        N = int(getInput())
        if N == 0:
            return
        
        departamentos = {}
        
        def novoDepartamento():
            Dep = getInput().split()
            Cod = Dep[0]
            Tipo = Dep[1]
            Con = float(Dep[2])

            if not Cod in departamentos.keys():
                departamentos[Cod] = Departamento(Cod, Tipo, Con)
            else:
                departamentos[Cod].consumo.append(Con)
        for i in range(N):
            novoDepartamento()
        
        for obj in departamentos.values():
            obj.calcMediaDepartamento()
            print(obj)
            if not obj in Tipo.departamentos.values():
                Tipo.departamentos[obj.tipo].append(obj)
        departamentos = None
        # pprint(departamentos)
        # pprint(tipos)
        pprint(Tipo.departamentos)
        pprint(Tipo.medias_tipos)

        # - Calcular o tipo de departamento com maior consumo médio, considerando a média dos consumos totais de todos os departamentos daquele tipo.
        # FEITO
        for array in Tipo.departamentos.values():
            for obj in array:
                print(obj)
                obj.calcMediasTipos(len(array))
        pprint(Tipo.medias_tipos)
        for tipo in Tipo.medias_tipos.keys():
            Mtipo = ""
            Mmedia = 0
            if Tipo.medias_tipos[tipo] > Mmedia:
                Mmedia = Tipo.medias_tipos[tipo]
                Mtipo = tipo
        print(Mtipo, Mmedia)
energia()
