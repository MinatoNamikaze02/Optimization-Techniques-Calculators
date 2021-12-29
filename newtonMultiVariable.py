import os
import numpy as np
from sympy import diff, symbols

x, y, z = symbols('x y z', real=True)
f = x - y + 2 * (x**2) + 2 * x * y + y**2

l = diff(f, x)
m = diff(f, y)


def lx(x, y):
    return 4 * x + 2 * y + 1


def mx(x, y):
    return 2 * x + 2 * y - 1


X1 = np.matrix([[0], [0]])
G = np.matrix([[lx(0, 0)], [mx(0, 0)]])

n = diff(l, x)
o = diff(m, y)
p = diff(l, y)
q = diff(m, x)

H = np.array([[n, p], [o, q]])
K = H.astype('float32')
J = np.linalg.inv(np.matrix(K))
F = J.dot(G)
X2 = X1 - F
print(type(X2))
print(X2)
print("=======================================================================")
x1 = X2[0]
y1 = X2[1]

print(lx(x1, y1))
print(mx(x1, y1))
# =============================================================================
# print(G.ndim,G.shape)
# print(l,m)
# print(l,m)
# print(lx(0,0))
# print(mx(0,0))
# print(H)
# print(J)
# print(F)
# print(K)
# =============================================================================