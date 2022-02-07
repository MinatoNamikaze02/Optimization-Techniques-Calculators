
import numpy as np
from scipy.optimize import fmin


from cli_mv import parseCLI


def f(x):
    return eval(expr)


res = parseCLI(type = "optimize")

if(res == False):
    init_expr = input("Enter the function in terms of x and y: ")
    expr = init_expr.replace("x", "x[0]").replace("y", "x[1]")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
else:
    [options, args] = res
    init_expr = str(options.fnc)
    expr = init_expr.replace("x", "x[0]").replace("y", "x[1]")
    print(expr)
    a = int(options.x1)
    b = int(options.x2)


min = fmin(f,np.array([a,b]))
print(min)

