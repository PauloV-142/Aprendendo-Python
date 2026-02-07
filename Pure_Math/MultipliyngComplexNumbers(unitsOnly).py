#The formula for multiplying complex numbers is:
# (a + ib) (c + id) = (ac - bd) + i(ad + bc)
complex1 = input('Insira um número complexo(ex:"2+3i"): ')
complex2 = input('Insira outro número complexo: ')
a = int(complex1[0])
c = int(complex2[0])
b = int(complex1[2])
d = int(complex2[2])
realResult = a*c - b*d
complexResult = a*d + b*c
finalComplex = str(realResult) + ' + ' + str(complexResult) + 'i'
print(f'The result is: {finalComplex}')