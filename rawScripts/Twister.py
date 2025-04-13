import random
start = input('Pressione Enter pra girar a roleta:')
pontos = 0
def step2():
    sort2 = random.randint(1, 6)
    if sort2 == 1:
        res = 'no 🔴'
    if sort2 == 2 :
        res = 'no 🔵'
    if sort2 == 3:
        res = 'no 🔶'
    if sort2 == 4:
        res = 'no ✅'
    if sort2 == 5:
        ran = random.randint(1, 4)
        if ran == 1:
            res = '🐶'
        if ran == 2:
            res = '🐺'
        if ran == 3:
            res = '🐔🐣🐓'
        if ran == 4:
            res = '🐷'      
    if sort2 == 6:
        res = '☁️'
    return res    
while start == '':
    sort1 = random.randint(1, 4)
    if sort1 == 1:
        resultado = 'Mão Direita '
    elif sort1 == 2:
        resultado = 'Mão Esquerda '
    elif sort1 == 3:
        resultado = 'Pé Direito '
    elif sort1 == 4:
        resultado = 'Pé Esquerdo '
    resultado = resultado + step2()
    print(resultado)
    print()
    start = input('Pressione Enter pra girar a roleta:')
    pontos += 1
print(f'Você fez {pontos} pontos!!')    