def sortAsc(*args: int):
    """Return numbers sorted. Ascending order."""
    n = list(args)
    l = len(n)

    def isSorted(array: list[int]|tuple[int]) -> bool:
        """Verifies if the list is sorted."""
        i = 0
        while i < l - 1:
            if not n[i] < n[i+1]:
                return False
            i += 1
        return True        

    def swap(i: int, j: int) -> None:
        """Swaps items i and j from a global list.\n
            Not for external use.                       """
        n[i], n[j] = n[j], n[i]

    i, j = 0, 1
    while not isSorted(n):
        if n[i] > n[j]:
            swap(i, j)
        # Pure mess, but works.
        i = i + 1 if i + 1 != l - 1 else 0
        j = i + 1 if i + 1 != 0 and i + 1 != l else 1
    return n

a, b, c, d = 5, 0, -3, 70
print(sortAsc(a, b, c, d))
# Output: [-3, 0, 5]