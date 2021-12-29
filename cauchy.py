from scipy.optimize import minimize

def f(x):
    return 4*x[0]**2 - 4*x[0]*x[1] + 2*x[1]**2

x0 = [2,3]
res = minimize(f, x0, method='CG',options= {"maxiter": 1, 'disp': True})
print(res.x)