from scipy.optimize import least_squares
import numpy as np
def f(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0]+x[1]**2-7)**2

x0 = np.array([1, 1])
res_1 = least_squares(f, x0)
print(res_1)
