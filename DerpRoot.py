print("""DerpRoot
Find the Nth root by trial and error!\n""")
index = int(input("Digite o índice da raiz: "))
radicand = int(input("Digite o radicando: "))#"".join(findroot)
derproot = "0" #["0"]
counter = 0
precision = 20
"""
while float("".join(findroot)) ** index != radicand or counter <= precision:
    for i in range(9):
        if float("".join(findroot)) ** index < radicand:
            findroot[len(findroot)-1] = str(i)
            print(findroot)
    findroot.append("0")
    counter += 1
"""
for i in range(precision):
    for j in range(10):
        if float(f"{derproot}{j}") ** index > radicand :
            derproot += str(j-1)
            break
    if float(f"{derproot}") ** index == radicand:
        break
print(derproot)
"""
droot(2, 2)
;0 ** 2 (0)> 4 False
;1 ** 2 (1)> 4 False
;2 ** 2 (4)> 4 False
;3 ** 2 (9)> 4 True
derproot = str(3-1)
"""


