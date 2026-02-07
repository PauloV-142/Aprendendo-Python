import time, string

def timer(func,):
    def wrapper(*args):
        start = time.time()
        print(func(args[0], args[1])[1])
        end = time.time()
        print((end-start), "s")
    return wrapper

@timer
def usingLists(n, source):
    res = []
    l = len(source)
    for i in range(n):
        res.append(source[i % l])
        res = res[:1]
    return res, "UsingLists: Done."

@timer
def usingStrings(n, source):
    res = ""
    l = len(source)
    for i in range(n):
        res += source[i % l]
    return res, "UsingStrings: Done."

if __name__ == "__main__":
    all = string.printable
    n = 9999999
    usingLists(n, all)
    print("-"*30)
    usingStrings(n, all)