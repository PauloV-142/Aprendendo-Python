def main():
    try:
        from math import sqrt
        print("Fórmula de Heron")
        print("Insira apenas números please")
        def normalize(a):
            if round(a) == a:
                return round(a)
            else:
                return a
        a = []
        sum = 0
        for i in range(0, 3):
            a.append(float(input(f"{i + 1}° lado: ")))
            sum += a[i]
        p = sum / 2
        print(f"O perímetro é: {normalize(sum)}")
        Heron = lambda a, p: sqrt(p * (p - a[0]) * (p - a[1]) *     (p - a[2]))
        print('A área é: ', normalize(Heron(a, p)))
        if Heron(a, p) == 0:
            print("Não é um triângulo")
    except ValueError as e:
        print(f"Um erro de valor surgiu!\n{e}")
    except Exception as e:
        print(f"Um erro surgiu!\n{e}")
main()
