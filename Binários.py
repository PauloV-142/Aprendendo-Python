def main():
    n = input("Insira um número Inteiro: ")
    def b(a):
        global n
        n = a
        if n != 1:
            n //= 2
            r = n % 3
            print(n, r)
            b(n)
    b(n)
    main()
main()
"""
if n == "":
    print("Insira um número!")
    main()
n = int(n)
if n <= 0:
    print("Insira um número positivo!")
    main()
"""