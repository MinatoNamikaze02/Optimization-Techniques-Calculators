import scipy.linalg as la
from sympy import symbols, hessian, Function, init_printing
import numpy as np
x, y, z = symbols('x y z')
f = symbols('f', cls=Function)
init_printing()

f = x**2 + 2*y**2 + 3*z**2 + 2*x*y + 2*x*z

H = hessian(f, (x, y, z))

eig = np.real_if_close(la.eigvals(np.array(H).astype('float')))

print(H)

if np.all(eig > 0):
    print("Positive Definite")
else:
    print("Not Positive Definite")