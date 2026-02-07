def calcTemp():
    while True:
        N = int(input())
        if N == 0: 
            return
        E = list(map(int, input().split()))
        MIN = int(min(E))
        MAX = int(max(E))
        MED = int(sum(E) / N)
        print(MIN, MAX, MED)
calcTemp()