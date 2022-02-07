"""


* FIBONACCI METHOD FOR SINGLE VARIATE OPTIMIZATION *
read more ---> http://web.tecnico.ulisboa.pt/mcasquilho/compute/com/,Fibonacci/pdfHXu_ch1.pdf
CHEERS!




"""


import numpy as np

from cli import parseCLI

e = np.exp(1)
pi = np.pi

def f(x):
    x = x
    return eval(fnc)

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


res = parseCLI(type='fib')
if(res == False):
    fnc = input("Enter the function as a String: ")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    n = int(input("Enter the number of iterations: "))
else:
    [options, args] = res
    fnc = options.fnc
    a = int(options.x1)
    b = int(options.x2)
    n = int(options.iter)
L = b-a
print('L = ',L)
k=2
while k<=n:
    print(f'------------Iteration - {k-1}--------------')
    I_0 = n-k+1
    I_1 = n+1
    F_0 = fib(I_0+1)
    F_1 = fib(I_1+1)
    Lk = (float(F_0)/float(F_1))*L
    print('I0 = ',I_0)
    print('I1 = ',I_1)
    print('F0 = ',F_0)
    print('F1 = ',F_1)
    print(f'L_{k} = ',Lk)
    x1 = a + Lk
    x2 = b - Lk
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
    fx1 = round(f(x1),2)
    fx2 = round(f(x2),2)
    print(f'f(x1) = {fx1}')
    print(f'f(x2) = {fx2}')
    if fx1 == fx2:
        a = x1
        b = x2
    elif fx1 > fx2:
        a = x1
    else:
        b = x2
    k+=1
    print('The values of a: ',a)
    print('The values of b: ',b)
print('-----------Answer------------')
print(f'The interval in which minimum lies [{a},{b}]')