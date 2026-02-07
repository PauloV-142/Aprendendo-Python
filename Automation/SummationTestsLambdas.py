OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '//': lambda a, b: a // b,
    '%': lambda a, b: a % b, 
    '**': lambda a, b: a ** b,
    'sqr': lambda a, b: a ** (1 / b),
    'odd': lambda a, b: a if a % 2 == 1 else 0,
    'even': lambda a, b: a if a % 2 == 0 else 0
}

class TestArray():
    def __init__(self, start=0, end=0):
        self.array = [i for i in range(start, end+1)]

    def apply_constant(self, constant: int, opr: str):
        c = constant
        chosen_operation =OPERATIONS[opr]
        return list(map(lambda x: chosen_operation(x, constant), self.array))

    def __str__(self):
       return str(self.array)

t1 = TestArray(start=0, end=2)
print(t1)
print(t1.apply_constant(4 , '/'))
# Result: 9
