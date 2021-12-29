from typing import no_type_check
import numpy as np

def f(x):
    return pow(x,3)-12.2*pow(x,2)+7.45*x+42      # enter first order derivative of your function here

def f_(x):
    return 3*pow(x,2)-24.4*x+7.45               # enter second order derivative of your function here

x = [0] * 20
x[0] = float(input("Enter the initial approximation (x0)\n"))

n = int(input("Enter the number or approximations you need \n"))

for i in range (0,n):
    x[i+1] = x[i] - (float)(f(x[i])/f_(x[i]))

print("{:<8} {:<25} {:<25} {:<25} {:<25} {:<25}".format('K','x[k]','x[k+1]','f(k)','f_(k)', 'f(k)/f_(k)'))
print('\n')

for i in range (0,n):
    print("{:<8} {:<25} {:<25} {:<25} {:<25} {:<25}".format(i,x[i],x[i+1],f(x[i]),f_(x[i]),f(x[i])/f_(x[i])))
