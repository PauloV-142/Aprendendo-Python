#Prime Madness
import time
def main():
    def normalize(b):
        if round(b) == b:
            return int(b)
        else:
            return b
    def pr(a):# 6
        n = 1
        p = True
        while n <= a // 2:# 2 <= 6 / 2
            n += 1# 2
            l = normalize(a / n)
            if type(l) == int: #4 / 2
                p = False
            if p == False:
                return p
        else:
            return p
    def returnpr(a):
        if pr(a) == True:
            return a
    s = int(input("Digite o tamanho da sequência: "))
    start = time.time()
    ns = 1
    a = 1
    primes = []
    while ns < s:
        ns += 1
        a += 1
        if pr(a) == True:
            primes.append(returnpr(a))
        ns = len(primes)
    else:
        print(primes)
        print("That's it!")
        end = time.time()
        print(round(end - start ,2))
    main()
main()