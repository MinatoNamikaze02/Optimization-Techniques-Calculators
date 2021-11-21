

# import numpy as np
import sys

sys.setrecursionlimit(5000)

def expression(x):
    return 2 * pow(x, 3) - 2 * x - 5                     # replace with your function here!

def findValA():
    for i in range (0, 10):
        exp = expression(i)
        if(exp<0):
            print(i)
            return i

def findValB():
    for i in range (0, 10):
        exp = expression(i)
        if(exp>0):
            print(i)
            return i


def step2(a,b):
    return b - ((expression(b)) / ((expression(b) - expression(a)) / (b - a)))


def recursion(a, b):
    z = step2(a,b)
    zd = expression(z)

    if(abs(zd) <= E):
        print("The most optimal solution is\n", z)
    else:
        if(zd>0):
            recursion(a,z)
        else:
            recursion(z,b)


changeE = input("Do you want to change E?")
if(changeE == 'y' or changeE=='Y'):
    E = input('Enter the new value of E')
    E = float(E)
else:
    E = pow(10, -3)

choice = input("Do you want to enter the values of x1 and x2\n")

if(choice == 'y' or choice=='Y'):
    a = input("Enter x1\n")
    a = int(a)
    b = input("Enter x2\n")
    b = int(b)
    recursion(a,b)
else:
    a = findValA()
    b = findValB()
    recursion(a,b)
