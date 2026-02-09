def calcBateria():
    while True:
        N = int(input())
        if N == 0:
            return
        if not 1 <= N <= 1000:
            return
        E = list(map(int, input().split()))
        E = list(map(lambda x: x * 9 / 10, E))
        print(int(sum(E)))
calcBateria()