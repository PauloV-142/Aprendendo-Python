# matrix = [[col+1 for col in range(2)] for row in range(2)]
# Unecessary difficult code to find the determinant of a matrix.
matrix = [[55, 76],[34, 87]]
print(matrix)
def det(mat):
    """Returns the determinant of a 2x2 matrix."""
    main = mat[0][0] * mat[1][1]
    sec = mat[0][1] * mat[1][0]
    # The unecessary part
    det = sec - main
    a = f"{det} = ({mat[0][1]} * {mat[1][0]}) - ({mat[0][0]} * {mat[1][1]})"
    d = f"{det} =   {sec} {" "*(list(a).index("-") - (12 + len(str(det))))}   -    {main}"
    print("\n", a ,"\n", d ,"\n")
    # End of the unecessary part
    return det
#print(det(matrix))

# Now print a Matrix knowing the determinant.
# (I mean all matrices, or a graph showing the values based on a determinant and the value of A11)

det = 1 #int(input("determinante"))
a = int(input("a11"))
matrix = [[a, ''],['' , '']]
det = a * matrix[1][1] - matrix[0][1] * matrix[1][0]