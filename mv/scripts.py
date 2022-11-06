import numpy as np
from scipy.interpolate import lagrange
from scipy.optimize import fmin, least_squares, minimize


def expression(x, func):
    x = x
    return eval(func)


def expr_multi(x, y, func):
    x = x
    y = y
    return eval(func)


# optimize
def downhill_simplex_primary(func: str, x1: float, x2: float) -> float:
    expr = func.replace("x", "x[0]").replace("y", "x[1]")
    min = fmin(expression, np.array([x1, x2]), args=(expr,), disp=False)
    return min


# least squares


def least_squares_primary(func: str, x1: float, x2: float) -> float:
    expr = func.replace("x", "x[0]").replace("y", "x[1]")
    x0 = np.array([x1, x2])
    res_1 = least_squares(expression, x0, args=(expr,))
    return res_1


# lagrange interpolation


def lagrange_interpolation_primary(func: str, x: list) -> float:
    if len(x) == 0:
        return
    x = np.array(x)
    y = eval(func)
    poly = lagrange(x, y)
    return str(poly).split("\n")[-1]


# cauchy gradient


def cauchy_gradient_primary(func: str, x1: float, x2: float, iter: int) -> float:
    x = [x1, x2]
    expr = func.replace("x", "x[0]").replace("y", "x[1]")
    f = lambda x: eval(expr)
    res = minimize(f, x, method="CG", options={"maxiter": iter or 1})
    return res.x
