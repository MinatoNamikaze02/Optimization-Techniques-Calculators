import numpy as np
import time

def f(x):
    fx = x**2 + (54/x) #Enter your function here
    return fx

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

def reg_elim(a,b,w1,w2,label):
    fw1 = f(w1)
    fw2 = f(w2)
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

def gs(a,b,it):
    i=0
    while i< it:
        upx = elim(a,b)
        w1 = upx[0]
        w2 = upx[1]
        label = reg(w1,w2)
        
        new_boundary = reg_elim(a,b,w1,w2,label)
        
        a = new_boundary[0]
        b = new_boundary[1]
        i+=1
        print('Iteration: ',i)
        print(a,b)
        time.sleep(1)

def main():
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    it = int(input('Enter number of iterations: '))
    gs(a,b,it)

main()