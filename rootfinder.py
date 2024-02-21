import scipy.optimize as op
import math

# def f(x):
#     return math.sin(x)

# x0 = 6
def rootFind(f, x0):
    op.fsolve(f, x0)

# rootFind(f, x0):