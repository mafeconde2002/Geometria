import numpy as np
import math
import matplotlib.pyplot as plt

def problem1 (p0,p1,p2):
    #Is p0p1 clockwise from p0p2 with respect to p0? 
    """
        INPUT: 
        3 arrays with coordenades (x,y)
        OUTPUT:
        bool: true if it's clockwise
    """
    p1=p1-p0
    p2=p2-p0
    cross = np.dot(p1, p2, out=None)
    norm_p1 = np.linalg.norm(p1) 
    norm_p2 = np.linalg.norm(p2) 
    angle = np.arccos(cross/(norm_p1*norm_p2))
    angle = angle%(2*math.pi)
    bool=False
    if angle <= math.pi:
        #if p1 and p2 are colineals it's clockwise
        bool=True
    return bool

def graph(p0,points):
    plt.quiver(p0, points[:, 0], points[:, 1], color=['blue','green'])
    plt.ylim(-10,10)
    plt.xlim(-10,10)
    plt.show()

p0=(3,4)
p1=(4,5)
p2=(2,1) 
points= np.array([p1,p2])
graph(p0,points)
