import numpy as np
def f(x):
    fx = x**2 + (54/x) #Enter your function here
    return fx

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

def main():
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    n = int(input('Enter n: '))
    L = b-a
    print('L = ',L)
    k=2
    while k<=n:
        print(f'------------Iteration - {k+1}--------------')
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
        fx1 = f(x1)
        fx2 = f(x2)
        print(f'f(x1) = {fx1}')
        print(f'f(x2) = {fx2}')
        if fx1 == fx2:
            a = x1
            b = x2
        elif fx1 > fx2:
            b = x2
        k+=1
        print('The values of a: ',a)
        print('The values of b: ',b)
    print('-----------Answer------------')
    print(f'The interval in which minimum lies [{a},{b}]')

main()