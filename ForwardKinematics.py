"""

Forward Kinematics

Author: Michelle Burroughs

"""



# 2D End Effector Position Generator
def fkposition2d(theta, l):
    import math
    size = len(theta)
    x = 0
    y = 0
    orientation = 0

    for k in range(size):# Convert to Radians
        theta[k] = math.radians(theta[k])

    for i in range(size):
        value = 0
        orientation += theta[i]

        for j in range(i):
            value += theta[j]

        x += l[i] * math.cos(value)
        y += l[i] * math.sin(value)

    return x, y, orientation


# 2D Transformation Matrix Generator
def tmatrix2d(theta,l):
    import math

    theta = math.radians(theta) #Convert to Radians

    r11 = math.cos(theta)
    r12 = -(math.sin(theta))
    r13 = l
    r21 = math.sin(theta)
    r22 = math.cos(theta)

    tmatrix = [[r11, r12, r13], [r21, r22, 0], [0, 0, 1]]

    return tmatrix


# 3D Transformation Matrix Generator
def tmatrix3d(theta, alpha, r, d):
    import math

    theta = math.radians(theta)# Convert to Radians
    alpha = math.radians(alpha)

    r11 = math.cos(theta)
    r12 = -(math.sin(theta)) * (math.cos(alpha))
    r13 = math.sin(theta) * math.sin(alpha)
    r21 = math.sin(theta)
    r22 = math.cos(theta) * math.sin(alpha)
    r23 = -(math.cos(theta) * math.sin(alpha))
    r31 = 0
    r32 = math.sin(alpha)
    r33 = math.cos(alpha)

    r41 = 0
    r42 = 0
    r43 = 0

    r14 = r * math.cos(theta)
    r24 = r * math.sin(theta)
    r34 = d
    r44 = 1

    tmatrix = [[r11, r12, r13, r14], [r21, r22, r23, r24], [r31, r32, r33, r34], [r41, r42, r43, r44]]

    return tmatrix



'''

The following functions describe 3D Forward Kinematic Matrix transformation

'''

# Rotation Matrix Around [X] Generator
def rotxmatrix3d(alpha):
    import math

    alpha = math.radians(alpha)# Convert to Radians

    r22 = math.cos(alpha)
    r23 = -(math.sin(alpha))
    r32 = -(math.sin(alpha))
    r33 = math.cos(alpha)

    rxmatrix = [[1, 0, 0, 0], [0, r22, r23, 0], [0, r32, r33, 0], [0, 0, 0, 1]]

    return rxmatrix


# Rotation Matrix Around [Z] Generator
def rotzmatrix3d(psi):
    import math

    psi = math.radians(psi)# Convert to Radians

    r11 = math.cos(psi)
    r12 = -(math.sin(psi))
    r21 = -(math.sin(psi))
    r22 = math.cos(psi)

    rzmatrix = [[r11, r12, 0, 0], [r21, r22, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

    return rzmatrix


# Translation Matrix Around [X] Generator
def transxmatrix3d(a):

    txmatrix = [[1, 0, 0, a], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

    return txmatrix


# Translation Matrix Around [Z] Generator
def transzmatrix3d(d):

    tzmatrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d,], [0, 0, 0, 1]]

    return tzmatrix


# Forward Kinematics Transformation Matrix Between i-1 and i 3D
def transmatrix3d(alpha, psi, a, d):
    import Matrices

    rotx = rotxmatrix3d(alpha)
    tx = transxmatrix3d(a)
    tz = transzmatrix3d(d)
    rotz = rotzmatrix3d(psi)

    tmatrix12 = Matrices.mmulti(rotx, tx)
    tmatrix23 = Matrices.mmulti(tmatrix12, tz)
    tmatrix = Matrices.mmulti(tmatrix23, rotz)

    return tmatrix


# Forward Kinematics Transformation From Base to End-Effector
def fktmatrix(alpha, psi, a, d):
    import Matrices

    size = len(alpha)
    tmatrix = [0] * size

    for i in range(size):
        tmatrix[i] = transmatrix3d(alpha[i], psi[i], a[i], d[i])

    tmatrix_combined = tmatrix

    for j in range(size-1):
        tmatrix_combined[j] = Matrices.mmulti(tmatrix_combined[j], tmatrix[j+1])


    return tmatrix_combined[size-1]


theta = [0,0,0]
alpha = [0,0,0]
r = [3,6,1]
d = [4,6,9]

print(fktmatrix(theta, alpha, r, d))

