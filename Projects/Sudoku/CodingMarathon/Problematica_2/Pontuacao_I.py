def calcPontos():
    while True:
        P, R = list(map(int, input().split()))
        if P == R == 0:
            return
        
        pontos = [0] * P
        
        # Rodadas
        for i in range(R):
            rodada = list(map(int, input().split()))
            for j, v in enumerate(rodada):
                pontos[j] += v

        print("Time", pontos.index(max(pontos)) + 1)

calcPontos()

