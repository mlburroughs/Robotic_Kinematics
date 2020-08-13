"""

Forward Kinematics

Author: Michelle Burroughs

"""

# 2D transformation matrix generator
def fkposition2d(theta, l):
    import math
    size = len(theta)
    x = 0
    y = 0
    orientation = 0

    for i in range(size):
        value = 0
        orientation += theta[i]
        for j in range(i):
            value += theta[j]

        x += l[i] * math.cos(value)
        y += l[i] * math.sin(value)

    return x, y, orientation

def tmatrix2d(theta,l):
    import math

    r11 = math.cos(theta)
    r12 = -(math.sin(theta))
    r13 = l
    r21 =

# 3D transformation matrix generator
def tmatrix3d(theta, alpha, r, d):
    import math
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