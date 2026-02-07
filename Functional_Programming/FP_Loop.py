# Functional Programming - Iterative
# Loop
def loop(num:int, func=lambda x: x, start=0) -> None:
    if num == start:
        return num
    # Script to iterate, BEFORE generating the stack
    # DESCENDING num - Building the call stack

    loop(num - 1, func, start=start)

    # Script to iterate, AFTER generating the stack
    # ASCENDING num - Dismounting the call stack
    func(num)
    return 

if __name__ == "__main__":
    m:int = lambda: 32
    print(loop(m(), lambda x: print("Hi world! Num:", x, )))

    