#def apagar(array,b):
#    c = ''
#    for i in array:
#        if i != b or i != '[' or i != ']':
#            c += i
#    return c
def apagar(array):
    c = ''
    for i in array:
        c += str(i)
    return c
def impar(array):
    c = ''
    for i in array:
        if i % 2 == 1:
            c += '🟩' + ' '
        else:
            c += '🟨' + ' '
    return c        
Layer = [1]
NextLayer = []
print(🟩)
for i in range(50):
    counter = 0
    for i in Layer:
        if counter == 0:
            NextLayer.append(i)
        counter = counter + 1
        try:
            b = Layer[counter]
        except:
            NextLayer.append(i)    
        else:
            NextLayer.append(i+b)
    print(apagar(impar(NextLayer)))
    Layer = NextLayer
    NextLayer = []        