def elevador():
    while True:
        N = int(input())
        if N == 0:
            return
        P = 0
        Max = 0
        for i in range(N):
            E, S = list(map(int, input().split()))
            P += E
            P -= S
            if P > Max:
                Max = P

        print(Max)


elevador()