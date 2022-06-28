from scipy.optimize import minimize
from cli_mv import parseCLI

def f(x):
    return eval(expr)


res = parseCLI(type = "cauchy")

if res == False:
    init_expr = input("Enter the function in terms of x and y: ")
    expr = init_expr.replace("x", "x[0]").replace("y", "x[1]")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    iter = int(input("Enter number of iterations: "))
else:
    [options, args] = res
    init_expr = str(options.fnc)
    expr = init_expr.replace("x", "x[0]").replace("y", "x[1]")
    a = int(options.x1)
    b = int(options.x2)
    iter = int(options.iter or 1)

x0 = [a,b]
res = minimize(f, x0, method='CG',options= {"maxiter": iter or 1, 'disp': True})
print(res.x)
