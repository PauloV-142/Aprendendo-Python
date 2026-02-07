def IP_Factorial(n): 
    "Programação Imperativa"
    res = 1
    for i in range(1, n+1): # Para começar em 1, e terminar em n.
        print("IP:", i)
        res = res * i
    return res

num = 9
print(f"Imperative Factorial of {num}: {IP_Factorial(num)}")


print("---")


def FP_Factorial(n): 
    "Programação Funcional, loops não são necessários."
    if n == 0:
        return 1
    print("FP:", n)
    return n * FP_Factorial(n - 1) # n vezes o antecessor dele mesmo.

num_ = lambda: 9
print(f"Functional Factorial of {num_()}: {FP_Factorial(num_())}")