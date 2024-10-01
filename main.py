n1 = float(input("Insira o primeiro número:\n"))
opr = str(input("Insira o operador:\n"))
n2 = float(input("Insira o segundo número:\n"))


def calcular(a, b):
    match opr:
        case "+":
            return a + b
        case "-":
            return a - b
        case "x":
            return a * b
        case "*":
            return a * b
        case "/":
            return a / b
        case "**":
            return a ** b
    
print(calcular(n1, n2))
