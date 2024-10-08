def main():
    x = float(input("x = "))
    opr = input("Operador:")
    y = float(input("y = "))
    def oprs(a, b):
        match opr:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                return a / b
            case "**":
                return a ** b
            case "//":
                global resto
                resto = a % b
                return a // b
        print(f"{x} {opr} {y} = {oprs(x, y)}")
        if opr == "//":
            print(f"resto: {resto}")

    res = input("Restart? ")
    if res == "y":
        main()
main()