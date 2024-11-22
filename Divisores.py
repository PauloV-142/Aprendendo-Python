def main():
    def normalize(b):
            if round(b) == b:
                return int(b)
            else:
                return b
    def divisores(a):
        Lista = [1]
        for i in range(a) :
            if a / (i + 1) == round(a / (i + 1)):
                Lista.append(i)
        return Lista
    
    n1 = int(input("Encontre os divisores de: "))
    print(divisores(n1))
    main()
main()