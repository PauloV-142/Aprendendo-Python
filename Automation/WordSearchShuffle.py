import time
#WordSearchShuffle
#From LetterShuffle.py

#Shuffle an array of characters on all possible manners
#1 Deal with repeated letters(Also from the original array);
#2 Look For syllabes.

#After Finished, I'll try to discover a more efficient way of shuffle.
#Differetial Suffle

start = time.time()
def doRepeat(array):
    if len(set(array)) == len(array):
        return True
    else:
        return False
def toStr(array):
    return ''.join(array)

def Shuffle(array:list):
    l = len(array)
    potencias = [0]*l
    neo = array[:]
    all = []
    for i in range(l):
        potencias[i] = l ** i

    for i in range(l ** l):
        for j in range(l):
            neo[j] = letters[(i//potencias[j])%l]
        if doRepeat(neo):
            all.append(toStr(neo))
    return all

letters = ['a','b','c','d','e','f','g','h']
Newarray = Shuffle(letters)
print(Newarray)
print(len(Newarray))

end = time.time()
print(end - start)
print('-'*30)


'''
vogals = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
CV (sa-la)
V (u-va)
VC (es-co-la)
CVC (car-ta)
CCV (pra-to)
CCVC (cris-tal)
CVCC (pers-pec-ti-va)
'''
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