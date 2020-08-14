"""
Matrices.py includes a library of function for use in matrix manipulation

Functions for computer matrices:
Matrix Addition: maddition(input1, input2)
Matrix Subtraction: msubtraction(input1, input2)
Matrix Multiplication: mmulti(input1, input2)
Matrix Scalar Multiplication: smmulti(input1, scalar)
Matrix Inversion: minverse(input1)
Matrix Transposition: mtranspose(input1)
Matrix Error Evaluation: matrixeval(input1, input2)

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


# Matrix Subtraction
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

#Scalar Matrix Multiplication
def smmulti(matrixin, scalar):

    r = len(matrixin[0])
    c = len(matrixin)
    matrixout = [r * [0] for _ in range(c)]

    for i in range(r):
        for j in range(c):
            matrixout[i][j] = matrixin[i][j] * scalar

    return matrixout

# Matrix Inversion
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


#Matrix Transposition Operation
def mtranspose(matrixin):

    r = len(matrixin[0])
    c = len(matrixin)
    tmatrix = [c * [0] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            tmatrix[i][j] = matrixin[j][i]

    return tmatrix


# Matrix Evaluation for Errors
def matrixeval(matrix1, matrix2):

    err1 = "Matrices are not compatible for addition or subtraction"
    err2 = "Matrices are not compatible for multiplication"

    if len(matrix1) != len(matrix2):
        print(err1)
    elif len(matrix1[0]) != len(matrix2[0]):
        print(err1)

    if len(matrix1[0]) != len(matrix2):
        print(err2)
    elif len(matrix2[0]) != len(matrix1):
        print(err2)

    return


# Rotational Operators

def rotationx(theta):
    import math

    theta = math.radians(theta)
    r22 = math.cos(theta)
    r23 = -(math.sin(theta))
    r32 = math.sin(theta)
    r33 = math.cos(theta)

    R_x = [[1, 0, 0], [0, r22, r23], [0, r32, r33]]

    return R_x


def rotationy(theta):
    import math
    theta = math.radians(theta)

    r11 = math.cos(theta)
    r13 = math.sin(theta)
    r31 = -(math.sin(theta))
    r33 = math.cos(theta)

    R_y = [[r11, 0, r13], [0, 1, 0], [r31, 0, r33]]

    return R_y


def rotationz(theta):
    import math
    theta = math.radians(theta)

    r11 = math.cos(theta)
    r12 = -(math.sin(theta))
    r21 = math.sin(theta)
    r22 = math.cos(theta)

    r_z = [[r11, r12, 0], [r21, r22, 0], [0, 0, 1]]

    return r_z


def rotation(theta):
    import math
    theta = math.radians(theta)

    r_x = rotationx(theta)
    r_y = rotationy(theta)
    r_z = rotationz(theta)

    r = mmulti(mmulti(r_z, r_y), r_x)

    return r
