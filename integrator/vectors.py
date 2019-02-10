import numpy as np

"""
This rotaional module given a vector and a number of revolutions will output a new vector.
"""

def rotMat(theta, vector):
    theta *=2*np.pi
    mat = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta),  np.cos(theta)]])
    return np.dot(mat,vector)

"""
Given a x,y cordinate and a previous vector and a number it will output:
    a list of points that neigbour x and y a distance of the vector.
    (Starting from the original vector direction and going counterclockwise
    or clockwise depending on the reverse parameter)
"""

def neighCor(x,y, prevV, N, reverse = False):
    pos = np.array([x,y])
    xV = prevV
    neigP =[]
    if N < 0:
        for i in range(N,0):
            rV = rotMat(i/N, xV)
            P=rV + pos
            neigP.append([P[0], P[1]])
    else:
        for i in range(N):
            rV = rotMat(i/N, xV)
            P=rV + pos
            neigP.append([P[0], P[1]])

    if reverse:
        return neigP[::-1]
    return neigP
