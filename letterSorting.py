import random
array = []
a = ""
while a != 'end':
    a = str(input("insira letras: "))
    if a != 'end':
        array.append(a)
print(f"{len(array)} Items.")
print(f"{len(array) * len(array)} possibilidades.")
for i in range(len(array) * len(array)):
    pass
'''
q w e <
e q w
w e q
q w e *
'''
'''
def walk(a):
    b = a[len(array) - 1]
    a.insert(0, b)
    a.pop(len(array) - 1)
    return a
'''