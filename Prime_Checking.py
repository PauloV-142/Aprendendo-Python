#Prime Checking
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
    print(pr(int(input("Digite um número: "))))
    main()
main()