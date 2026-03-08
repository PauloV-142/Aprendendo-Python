import instant_input
# TERMINAL CHECK: Verify the lenght of a line on the terminal line via user assistance.

def add10():
    arr = "0123456789"
    count = 0
    key = input("Press Enter to add new chars.\nOr type the number where the line ends.\n")
    while True:
        if key not in list(arr):
            print(arr, flush=True, end="")
        else:
            end_num = (count * 10) - (10 - (int(key) + 1))
            print("\nThe line has", end_num, "chars.")
            return end_num
        key = get_input()
        count += 1

if __name__ == "__main__":
    print(n := add10())
    print("a" * n)
    data = f"LEN={n}"