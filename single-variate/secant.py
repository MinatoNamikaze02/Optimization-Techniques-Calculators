"""


* SECANT METHOD FOR SINGLE VARIATE OPTIMIZATION *
read more ---> https://en.wikipedia.org/wiki/Secant_method#:~:text=In%20numerical%20analysis%2C%20the%20secant,difference%20approximation%20of%20Newton's%20method.
CHEERS!




"""




from sympy import *
import numpy as np
import sys

import optparse
from cli import parseCLI
#CLI args
parser = optparse.OptionParser()

e = np.exp(1)
pi = np.pi
sys.setrecursionlimit(10000)

def expression(x):
    x = x
    return eval(fnc)         

def step2(a,b):
    return b - ((expression(b)) / ((expression(b) - expression(a)) / (b - a)))

def printfn(z):
    print("The derivative of the function is: ", fnc)
    print("The initial value x1: ", x1)
    print("The initial value x2: ", x2)
    print("E: ",E)
    print("The most optimal solution is: ", z)

def recursion(a, b):
    z = step2(a,b)
    zd = expression(z)
    if(abs(zd) <= E):
        printfn(z)
    else:
        if(zd>0):
            recursion(a,z)
        else:
            recursion(z,b)

res = parseCLI()
if(res == False):
    x = symbols('x')
    inp = input("Enter the function as a String: ")
    expr = Derivative(inp, x)
    fnc = str(expr.doit())
    x1 = int(input("Enter the limit x1: "))
    x2 = int(input("Enter the limit x2: "))
    choice = input("Do you want to change E (default 0.001)? (y/n)")
    if choice=='y' or choice=='Y':
        E2 = input("Enter the value of E")
    else:
        E2 = None
else:
    [options, args] = res
    x = symbols('x')
    expr = Derivative(options.fnc, x)
    fnc = str(expr.doit())
    E  = 0
    E2 = options.E2
    x1 = options.x1
    x2 = options.x2
if not E2:
    E = 10**-3
else:
    E = eval(E2)

try:
    recursion(int(x1), int(x2))
except ValueError:
    print("\nIncorrent values entered for x1 or x2, please retry..")
