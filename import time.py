import time
def main():
    a = []
    def t():
        start = time.time()
        time.sleep(0)
        end = time.time()
        e = start - end
    #    print(e)
        a.append(e)
    b = 1
    c = int(input("Iterations: "))
    while b < c:
        b += 1
        time.sleep(0)
        t()
    else:
        m = sum(a) / len(a)
        print(a)
        print(f"Média {m}")
    main()
main()