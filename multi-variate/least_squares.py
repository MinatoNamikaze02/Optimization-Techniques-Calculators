from scipy.optimize import least_squares
import numpy as np
from cli_mv import parseCLI

def f(x):
    return eval(expr)


res = parseCLI(type = "leastsq")
if res == False:
    init_expr = input("Enter the function in terms of x and y: ")
    expr = init_expr.replace("x", "x[0]").replace("y", "x[1]")
    a = input("Enter a: ")
    b = input("Enter b: ")
else:
    [options, args] = res
    init_expr = str(options.fnc)
    expr = init_expr.replace("x", "x[0]").replace("y", "x[1]")
    a = options.x1
    b = options.x2

x0 = np.array([a, b])
res_1 = least_squares(f, x0)
print(res_1)
