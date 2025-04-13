#Differetial Suffle
import time
start = time.time()
'''
import math
print('-'*30)
letters = ['a','b','c','d']
all = []
for i in letters:
    for j in letters:
        for k in letters:
            for l in letters:
                neo = i+j+k+l
                if neo.count(i) == 1 and neo.count(j) == 1 and neo.count(k) == 1 and neo.count(l) == 1:
                    all.append(neo)
print(all)
all = []
neo = letters
counter = 0
letters = ['a','b','c','d']
for i in range(4**4):
    if i/64 == int(i/64):
        neo[0] = letters[int(i/64)%4]
    if i/16 == int(i/16):
        neo[1] = letters[int(i/16)%4]
    if i/4 == int(i/4):
        neo[2] = letters[int((i/4)%4)]
    if i == i:
        neo[3] = letters[i%4]
        if neo.count(neo[0]) == 1 and neo.count(neo[1]) == 1 and neo.count(neo[2]) == 1 and neo.count(neo[3]) == 1:
            print(neo) 
            counter += 1
print(counter)'
'''
def toStr(array):
    return ''.join(array)

def inffor(array):
    l = len(array)
    potencias = [0]*l
    neo = array[:]
    all = []
    for i in range(l):
        potencias[i] = l ** i

    for i in range(l ** l):
        for j in range(l):
            neo[j] = letters[(i//potencias[j])%l]
        if len(set(neo)) == l:
            all.append(toStr(neo))
    return all
letters = ['a','b','c','d']
reorganizations = inffor(letters)
print(reorganizations)
print(len(reorganizations))
'''
print('*'*3)

l = len(letters)
potencias = [0] *l
neo = letters[:]
for i in range(l):
        potencias[i] = l ** i

for i in range(l**l):
    for j in range(l): #0 | 1 | 2 | 3 
        neo[j] = letters[(i//potencias[l-j-1])%l]
    print(neo)
'''
end = time.time()
print(end - start)
print('-'*30)
