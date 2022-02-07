"""


* NEWTON RAPHSON METHOD FOR SINGLE VARIATE OPTIMIZATION *
read more ---> https://www.math.ubc.ca/~anstee/math104/newtonmethod.pdf
CHEERS!




"""


import numpy as np
from sympy import *
from cli import parseCLI
e = np.exp(1)

def f(x):
    x = x
    return eval(func)

def f_(y):
    x = symbols('x')
    expr = Derivative(func, x)
    der = expr.doit()
    x = y
    return eval(str(der))



res = parseCLI(type = "newt")
if(res == False):
    func = input("Enter the function as string: ")
    x = float(input("Enter the initail approximation (x0)\n"))
    n = int(input("Enter the number or approximations you need \n"))
else:
    [options, args] = res
    func = options.fnc
    x = int(options.x1 )
    n = int(options.iter)
val = []
val.append(x)

for i in range (0,n):
    temp = val[i] - (float)(f(val[i])/f_(val[i]))
    val.append(temp)

for i in range(0, len(val)):
    print("Value after iteration " + str(i) + " :" + str(val[i]))



"""
print("{:<8} {:<25} {:<25} {:<25} {:<25} {:<25}".format('K','x[k]','x[k+1]','f(k)','f_(k)', 'f(k)/f_(k)'))
print('\n')

for i in range (0,n):
    print("{:<8} {:<25} {:<25} {:<25} {:<25} {:<25}".format(i,x[i],x[i+1],f(x[i]),f_(x[i]),f(x[i])/f_(x[i])))

"""



