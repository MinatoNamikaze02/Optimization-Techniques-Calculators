
import numpy as np
from sympy import diff, false, symbols

from cli_mv import parseCLI
x,y,z = symbols('x y z')

res = parseCLI(type = "newton-mv")

if res == False:
    f = input("Enter the function as a string...(not more than 3 vars ^^)")

else:
    [options, args] = res
    f = str(options.fnc)



l = diff(f, x)
m = diff(f, y)

ls = str(l)
ms = str(m)

def lx(x, y):
    x = x
    y = y
    return eval(ls)


def mx(x, y):
    x = x
    y = y
    return eval(ms)

X1 = np.matrix([[1], [1]])
G = np.matrix([[lx(1, 1)], [mx(1, 1)]])

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
