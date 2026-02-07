print('Cores disponíveis no terminal:')
r1 = list(range(0,9))+[21,22]
r2 = list(range(30,36))+list(range(40,47))+[53]
r3 = list(range(90,96))+list(range(100,107))

for i in r1+r2+r3:
    print(f'{i}\033[{i}m','0'*30,'\033[0m')