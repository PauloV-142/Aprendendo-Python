def drones():
    while True:
        N = int(input())
        if N == 0:
            return
        
        pontos = [0] * N
        
        # Rodadas
        for i in range(N):
            velocidades = list(map(int, input().split()))
            # print(velocidades)
            pontos[i] += sum(velocidades)

        print("Drone", pontos.index(max(pontos)) + 1)

drones()
