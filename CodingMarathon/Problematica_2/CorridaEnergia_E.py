def corrida():
    
    while True:
        min = 0
        R = 0
        N = int(input())
        if N == 0:
            return
        
        trajeto = list(map(int, input().split()))

        for i in trajeto:
            if R < min:
                min = R
            R = R + i
        
        print(int(R))
        print(min)

corrida()