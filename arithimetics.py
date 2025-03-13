import time
import math
opr = ""
def main():
    global opr
    x = float(input("x = "))
    if bool(opr) == False:
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
    time.sleep(math.pi / math.e)
    res = input(f"Press enter to restart:\n n to quit:\nOr select another operator: ")
    if res == "n":
        pass
    elif type(res) == str:
        opr = res
        main()
main()