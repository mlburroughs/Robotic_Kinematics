"""
Functions for computer matrices

Author: Michelle Burroughs

"""

matrix1 = [[1,2,3],[3,4,3]]
matrix2 = [[1,2],[1,2],[1,2]]


# Matrix Addition
def maddition(matrix1, matrix2):

    #columns
    c1 = len(matrix1)
    c2 = len(matrix2)

    #rows
    r1 = len(matrix1[0])
    r2 = len(matrix2[0])

    #matrix = c1*[c2*[0]]
    matrix = [c2 * [0] for _ in range(c1)]

    for i in range(r1):
        for j in range(c1):

            m1 = matrix1[i][j]
            m2 = matrix2[i][j]
            newitem = m1 + m2
            #print(f"m1: {m1} m2: {m2} newitem: {newitem}")
            matrix[i][j] = newitem
            #print(matrix)

    return matrix


# Matrix subtraction
def msubtraction(matrix1, matrix2):

    #columns
    c1 = len(matrix1)
    c2 = len(matrix2)

    #rows
    r1 = len(matrix1[0])
    r2 = len(matrix2[0])

    matrix = [c2 * [0] for _ in range(c1)]

    for i in range(r1):
        for j in range(c1):

            m1 = matrix1[i][j]
            m2 = matrix2[i][j]
            newitem = m1 - m2
            #print(f"m1: {m1} m2: {m2} newitem: {newitem}")
            matrix[i][j] = newitem
            #print(matrix)

    return matrix


# Matrix Multiplication
def mmulti(matrix1, matrix2):

    c1 = len(matrix1)
    c2 = len(matrix2)

    #rows
    r1 = len(matrix1[0])
    r2 = len(matrix2[0])

    matrix = [r2 * [0] for _ in range(c1)]

    for i in range(r2):
        for j in range(c1):
            for k in range(r1):
                matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return matrix


# matrix inverse
def minverse(matrixin):

    col = len(matrixin)
    r = len(matrixin[0])

    # identity matrix
    idmatrix = [r * [0] for _ in range(col)]
    for i in range(r):
        for j in range(col):
            if i == j:
                idmatrix[i][j] = 1

    if col == 2:# 2 X 2 matrix
        a = matrixin[0][0]
        b = matrixin[0][1]
        c = matrixin[1][0]
        d = matrixin[1][1]

        determinant = (a*d) - (b*c)
        matrixint = [[d, -b], [-c, a]]
        det = (1/determinant)
        invmatrix = [r * [0] for _ in range(col)]
        for i in range(col):
            for j in range(col):
                invmatrix[i][j] = matrixint[i][j]*det

    elif col == 3:# 3X3 matrix
        a = matrixin[0][0]
        b = matrixin[0][1]
        c = matrixin[0][2]
        d = matrixin[1][0]
        e = matrixin[1][1]
        f = matrixin[1][2]
        g = matrixin[2][0]
        h = matrixin[2][1]
        i = matrixin[2][2]

        matrixminor = [r * [0] for _ in range(r)] #matrix of minors
        matrixminor[0][0] = (e*i) - (h*f)
        matrixminor[0][1] = -((d*i) - (g*f))
        matrixminor[0][2] = (d*h) - (g*e)
        matrixminor[1][0] = -((b*i) - (h*c))
        matrixminor[1][1] = (a*i) - (g*c)
        matrixminor[1][2] = -((a*h) - (g*b))
        matrixminor[2][0] = (b*f) - (e*c)
        matrixminor[2][1] = -((a*f) - (d*c))
        matrixminor[2][2] = (a*e) - (d*b)

        tmatrix = matrixminor
        tmatrix[0][1] = matrixminor[1][0]
        tmatrix[0][2] = matrixminor[2][0]
        tmatrix[1][0] = matrixminor[0][1]
        tmatrix[1][2] = matrixminor[2][1]
        tmatrix[2][0] = matrixminor[0][2]
        tmatrix[2][1] = matrixminor[1][2]

        determinant = (a * matrixminor[0][0]) - (b * matrixminor[0][1]) + (c * matrixminor[0][2])
        det = 1/determinant
        invmatrix = [r * [0] for _ in range(r)]
        for i in range(r):
            for j in range(r):
                invmatrix[i][j] = det * tmatrix[i][j]

    else:# matric 4X4 or larger
        invmatrix = 0

    return invmatrix


def mtranspose(matrixin):

    r = len(matrixin[0])
    c = len(matrixin)
    tmatrix = [c * [0] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            tmatrix[i][j] = matrixin[j][i]

    return tmatrix



matrixin = [[2,6],[2,4],[2,2],[1,5]]
print(mtranspose(matrixin))