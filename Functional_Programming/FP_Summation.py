# FP_Summation - Iterative
def summ(num:int, func=lambda x: x) -> int:
    if num < 2:
        return 1
        
    return num + summ(num - 1)

# GaussSummation
gSumm:int = lambda num: (num * (num + 1)) // 2

printLoop = lambda x, f=lambda y: y, start=0: loop(x, func=lambda x: print(f(x)), start=start)

if __name__ == "__main__":
    from FP_Loop import loop
    m = lambda: 4

    printLoop(m(), gSumm, start=0)
    print()
