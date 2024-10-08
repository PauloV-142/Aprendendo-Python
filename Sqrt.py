def main():
    print("Raíz quadrada pelo método de Newton.")
    n = float(input("Digite um número:"))
    guess = 1
    def root():
        global r
        r = 1 / 2*((n * guess) + guess)
        if guess == r:
            print(r)
        else:
            guess = r
            root()
        root()
    main()
main()