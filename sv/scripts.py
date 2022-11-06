import sys

from sympy import Derivative, symbols

# a recursion limit set for secant method
sys.setrecursionlimit(5000)

E = 10 ** -3

def change_E(new_E):
    global E
    E = new_E

# secant
def expression(x, func):
    x = x
    return eval(func)         

def step2(a, b, func):
    return b - ((expression(b, func)) / ((expression(b, func) - expression(a, func)) / (b - a)))

def recursion(a, b, func) -> float:
    z = step2(a, b, func)
    zd = expression(z, func)
    if(abs(zd) <= E):
        return z
    else:
        if(zd>0):
            return recursion(a, z, func)
        else:
            return recursion(z, b, func)

def secant_primary(func: str, x1: float, x2: float, E: float = 10**-3)-> float:
    change_E(E)
    x = symbols('x')
    expr = Derivative(func, x)
    fnc = str(expr.doit())
    return recursion(x1, x2, fnc)
# newton

def f_(y, func):
    x = symbols('x')
    expr = Derivative(func, x)
    der = expr.doit()
    x = y
    return eval(str(der))

def newton_primary(func: str, x: float, n: int, E: float = 10**-3)-> float:
    change_E(E)
    val = []
    val.append(x)
    for i in range (0,n):
        if f_(val[i], func) == 0:
            print("Error: Division by zero")
            return
        temp = val[i] - (float)(expression(val[i], func)/f_(val[i], func))
        val.append(temp)
    return val[-1]

# Fibonacci

def fib(n):
    a=0
    b=1
    if n == 0:
        return a
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    return b

def fibonacci_primary(fnc: str, a: float, b: float, n: int, E: float = 10**-3):
    change_E(E)
    k=2
    L = b-a
    while k <= n:
        I_0 = n-k+1
        I_1 = n+1
        F_0 = fib(I_0+1)
        F_1 = fib(I_1+1)
        Lk = (float(F_0)/float(F_1))*L
        x1 = a + Lk
        x2 = b - Lk
        fx1 = round(expression(x1, fnc),2)
        fx2 = round(expression(x2, fnc),2)
        if fx1 == fx2:
            a = x1
            b = x2
        elif fx1 > fx2:
            a = x1
        else:
            b = x2
        k+=1
    return a, b

# golden section search

def reg(w1,w2):
    if w2 < w1:
        label = 'right'
    else:
        label = 'left'
    return label

def elim(a,b):
    d = 0.618*(b-a)
    w1 = a + d
    w2 = b - d
    return w1,w2

def reg_elim(fnc, a, b, w1, w2, label):
    fw1 = expression(w1, fnc)
    fw2 = expression(w2, fnc)
    if label == 'right' and fw2>fw1:
        a = w2
        b = b
        upx = elim(a,b)
        w1 = upx[0]
        w2 = upx[1]
    else:
        a = a
        b = w1
        upx = elim(a,b)
        w1 = upx[0]
        w2 = upx[1]
    return a,b,w1,w2

def golden_section_primary(fnc: str, a: int , b: int, it: int, E: float = 10**-3):
    change_E(E)
    i=0
    while i < it:
        upx = elim(a,b)
        w1 = upx[0]
        w2 = upx[1]
        label = reg(w1,w2)
        
        new_boundary = reg_elim(fnc, a, b, w1, w2, label)
        
        a = new_boundary[0]
        b = new_boundary[1]
        i+=1
    return a,b
