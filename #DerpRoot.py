def main():
    index = int(input("Digite o índice: "))
    radicand = float(input("Radical: "))
    precision = 20
    root = 0
    counter = 0
    decroot = [0] * (precision+1)
    while root ** index <= radicand:
        root += 1
    root -= 1
    print(root)
    decroot[0] = root
    if root ** index != radicand:
        for i in range(precision):
            for j in range(10):
                decroot[i+1] = decroot[i] + j/10**i
                if decroot[i+1] ** index > radicand:
                    break
            decroot[i+1] -= 1/10**i
            print(decroot[i+1])    
    main()
main()    