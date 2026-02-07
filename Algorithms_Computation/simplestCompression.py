def compress_(binaries:list[int]) -> tuple[int]:
    compressed = []
    for binary in binaries:
        compressed.append(compress(binary))
    return tuple(compressed)

# Simplest Compression
# 00000 -> 5

# THIS CODE IS ONLY DEMONSTRATIVE - NOT RELIABLE
# By returning a string, the result, whose should be compressed by the function's purpose, will, in fact be bigger than the input, making *this* function, as it is now, useless.
# Why is that?
# 1. The return value, a string, is a list of characters. A character is a 8bit, a.k.a. 1byte representation of an integer, that is presented as a readable character for the user.
# 2. Thus, the characters '0' and '1', are, in storage: 0b0000000000 and 0b0000000001. A byte long.
# What a mess we've built there. The resulting string is, in storage, a multiple of those dummy bytes. Way longer than the input was.

# The correct way would be returning:
# 1. Something that indicates that this is a compressed value, that can be a file extension. e.g. +'.gut'.
# 2. A integer, whose it's Base10* representation is what maps the compression.

# *Problem, Base10 only has 9 usable characters, what means that:
# 1. If the input has more than, 9 zeros in a row, it's representation would be a 2-digit number, that would totally mess up with the discompression.
# 2. Base10 is intended for human usage, thus, trying to use it in a mostly low-level operation, such as compression, isn't reliable. And brings problems along.

# Solution, returning a Tuple of integers. Thus, they're separated by the data type's properties.
# It brings a problem with it. I'm not sure, but I think that Tuples are not back-to-back in memory, and linked by pointers, what usually have 8bytes long. Not that reliable.
# Thus, the final solution would be returning a array, whose data is actually back-to-back in memory. Saving lots of bytes, the main purpose of compression after all.
# ;)

def str_compress(bin:str) -> str:
    current = bin[0]
    compressed = [0]
    counter = 0
    for bit in bin:
        if bit != current:
            counter += 1
            current = bit
            compressed.append(0)
        compressed[counter] += 1
    result = ""
    for i in compressed:
        result += str(i)
    return int(result)

def compress(binary:int) -> tuple[int]:
    # The lenght of a binary number. [x]Don't use strings. bin()
    LENGHT:int = len(bin(binary)[2:])
    current = binary[0]
    compressed = [0]
    counter = 0
    for pos in range(LENGHT): # pos = 0, 1, 2, 3, 4, 5
        if binary & ~2 << pos: # 0, 1, 2, 4, 8, 16
            0
    return bin #tuple([bin])


if __name__ == "__main__":
    binaries = (
        0b0000_0000_0000_0001,
        0b0000_0000_0000_0011
        )

    # print(compress_(binaries))
    import sys
    from time import time
    sys.set_int_max_str_digits(1000000)
    m = 1000
    start2 = time()
    b = 2 << m
    end2 = time() - start2
    print(end2)

    start1 = time()
    a = 3 ** m
    end1 = time() - start1
    print(end1, a == b, sep="\n")