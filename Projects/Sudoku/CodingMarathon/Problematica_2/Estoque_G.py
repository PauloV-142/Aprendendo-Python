def calcEstoque():
    while True:
        N = int(input())
        if N == 0:
            return
        
        estoque = list(map(int, input().split()))
        P = int(input())
        comp = list(map(int, input().split()))
        for i in comp:
            i -= 1
            
            if estoque[i] != 0:
                estoque[i] -= 1 
        # print(estoque)
        print(sum(list(map(lambda x: 1 if x != 0 else 0, estoque))))
        print(estoque.count(0))

calcEstoque()