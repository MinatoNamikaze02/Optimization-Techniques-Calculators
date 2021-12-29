import numpy as np
from scipy.optimize import fmin
import math

def f(x):
    return x[0] - x[1] + 2*x[0]**2 + 2*x[0]*x[1] + x[1]**2

min = fmin(f,np.array([0,0]))
print(min)