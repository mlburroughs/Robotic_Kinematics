"""

Matrix Evaluation Functions for Robotics


Author: Michelle Burroughs

"""


# Evaluation of degress of freedom where n_parameters is the number of available positions
# such as 3 positions, 3 orientations; n_contraints is the number of dof contraints
# for example 1 dof contraint for n joints
def dofsyseval(n_parameters, n_contraints):

    dof = n_parameters - n_contraints
    return dof


# Evaluation of redundancy where n is number of links and m_0 is number of degrees of freedom
# in end effector
def redundancyeval(n, m_0):

    redeval = 0
    if n > m_0:
        print('System is Redundant')
        dor = n - m_0
        redeval = 1
    elif n == m:
        dor = 0

    return dor, redeval