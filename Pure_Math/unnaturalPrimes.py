# 23 / 7 / 2025
# FreeCodeCamp daily exercise.
from math import isqrt

def is_unnatural_prime(n: int) -> bool:
    """
    Determines if a number is a "unnatural prime".

    A number is prime when it's only divisible by 1 and itself.
    Works for both positive and negative numbers.

    Parameters:
        n (int): the number to check. Any integer.
    
    Returns:
        bool: True if is a prime; False otherwise.
    
    Raises:
        ValueError: If the input is not an integer
    ---
    ### 23 / 7 / 2025
    ### FreeCodeCamp daily exercise.
    """
    if type(n) != int:
        raise ValueError("N must be a integer.")

    abs_n = abs(n) # Allows for negatives.
    if abs_n <= 1:
        return False # 0 and 1 aren't primes.

    # Mathematical tweak for efficiency.
    upperBound = isqrt(abs_n)
    for i in range(2, upperBound):
        if abs_n % i == 0:
            return False
    return True