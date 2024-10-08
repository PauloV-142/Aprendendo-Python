print("Raíz quadrada pelo método de Newton.")
def main():
    n = float(input("Digite um número:"))
    def Sqrt(a):
        guess = a
        r = 1
        while guess != r:
            guess = r
            r = ((a / guess) + guess)/2
        else:
            return round(r, 2)
    print(Sqrt(n))
    main()
main()