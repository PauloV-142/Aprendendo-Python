def main():
    def normalize(b):
            if int(b) == b:
                return int(b)
            else:
                return b
    def divisores(a):
        Lista = []
        for i in range(1,a):
            if a / (i) == round(a / (i)):
                Lista.append(i)
        Lista.append(a)
        return Lista
    
    n1 = int(input("Encontre os divisores de: "))
    print(divisores(n1))
    main()
main()