# you have a b c, they are all algarisms different from zero.
# when you do ab * c what. values will give you 'aaa' 3 times that algarism?

def test(a, b, c):
    ab = int(str(a) + str(b))
    res = ab*c
    for n in str(res):
        if n != str(a):
            return 0
    print(f'{ab}*{c}={ab*c}')#, {"True!!!!!" if str(res) == str(a)*3 else False}')
    
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            test(a,b,c)
# we could guess a 3 digit number, and then factor it ourselves ;-;
# 37*9=333, True!!!!!           