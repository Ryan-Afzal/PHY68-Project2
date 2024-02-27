

# define potential equation modeled by a deep square well and then a boundary 
# defined by the coulomb reulsive force
import numpy as np
from scipy import constants as const
from scipy import sparse as sparse
from scipy.sparse.linalg import eigs
from matplotlib import pyplot as plt
Z = 86
A = 212
r = 1.2 * ((4)**(1/3) + A**(1/3)) # nuclear separation
def potential(Z, x) :
    if x < r :
        return 0
    else :
        return ((2 * 1.44 * (Z - 2))/ (x)) 

