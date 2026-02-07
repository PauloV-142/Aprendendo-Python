def fibonacci(i:int, func=lambda x: x) -> int:
    if i < 1:
        return 1
    
    return fibonacci(i - 1) + fibonacci(i - 2)

def loop(i, func=lambda x: x) -> None:
    if i == 0:
        return 1
    loop(i - 1, func)
    
    return func(i)

if __name__ == "__main__":
    # printLoop = lambda x, f: loop(x, lambda: print(f))

    print(fibonacci(1))
