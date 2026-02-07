
for i in range(20):
    print(num := int(input("Integer: ")), "Is not a prime!" if True in [True if int(num / i) == num / i else False for i in range(2, num)] else "Is a prime!")