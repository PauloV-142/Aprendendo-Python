# Recamàn sequence
""" A path on a number line.
The sequence can be represented visually (pathways), and numerically (distances & signals).

START at 1.
[1]

Priorize going backwards. BUT
    IF you can go backwards AKA is the spot (your position - i) avaliable?:
        THEN go backwards by the value of i. In other words, occupy that spot.
    
    ELIF you can't go backwards:
        THEN go forward by the value of i. In other words, occupy that spot.
    
    INCREMENT i by 1.
    REPEAT [line 8.]

"""

# Functional programming

def canRetrocess(i, pos, seq) -> bool:
    if i > pos:
        return False
    return seq[pos - i]

def new(max):
    return [True]*max

def recaman(i, pos, seq, max):
    if i >= max:
        return seq
    if canRetrocess(i, pos, seq):
        raise NotImplementedError
        
        
if __name__ == "__main__":
    print(recaman(1, 1, new(max), max))