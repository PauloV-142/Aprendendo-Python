#"Don't know" the Van Eck Sequence
#00102022160502654053032904936'14'...
#The next number is based on
# the question about the present value of
# n(the present number):
#I've seen that number before? How much before?
#The distance of the last aparição of the number
# is the next value.
import time
InitialValue = 0
VanEckSeq = []
VanEckSeq.append(InitialValue)
VanEckSeq.append(0)
print(VanEckSeq)

def invert(seq):
    inverted = []
    for i in range(len(seq)):
        inverted.append(seq[-(i+1)])
    return inverted
    
def search(seq):
     counter = 0
     nLastValue = seq[-1]
     lastIndex = len(seq)-1
     inverted = invert(seq)
     for i in inverted:
         if counter > 0:
             if i == nLastValue:
                 return counter
         counter += 1
     return 0    
for i in range(30):         
    VanEckSeq.append(search(VanEckSeq))
print(VanEckSeq)
print('00102022160502654053032904936.14...')
for i in VanEckSeq:
    dot = ''
    for j in range(i):
        dot = dot + '|'
    dot = dot + '.'    
    print(dot)    