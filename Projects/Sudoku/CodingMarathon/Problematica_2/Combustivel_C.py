def calcCombustivel():
    while True:
        N = int(input())
        if N == 0:
            return
        EN = []
        ENMedias = EN.copy()
        ENMelhor = EN.copy()
        for i in range(N):
            def kml(list):
                print(list)
                for j in range(len(list)):
                    list[j] = list[j][1] / list[j][0]
                print(list)
                return list
            ENMedias.append(list(map(lambda x: int(x) , input().split())))
        MEL = max(kml(ENMelhor))
        print(ENMelhor)
        L = 0
        K = 0
        for i in range(len(ENMelhor)):
            L += ENMelhor[i][0]
            K += ENMelhor[1][1]
            print(i)
        # MED = sum(EN) / N

        print("Media:", K / L)
        print("Melhor:", MEL)

calcCombustivel()