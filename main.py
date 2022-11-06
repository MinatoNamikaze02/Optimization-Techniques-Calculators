import click

from sv import scripts as sv_utils
from mv import scripts as mv_utils

allowed_methods = ['sec', 'newt', 'fib', 'GS', 'DS', 'lagin', 'ls', 'CG']

@click.command()
@click.argument('type', nargs=1)
@click.option('--func', '-f', type=str, help='Function to be optimized')
@click.option('--first', '-x1' , type=float, default=None, help='First value of x')
@click.option('--second', '-x2', type=float, default=None, help='Second value of x')
@click.option('--third', '-x3', type=float, default=None, help='Third value of x')
@click.option('--iter', '-i', type=int, default=None, help='Number of iterations')
@click.option('--epsilon', '-e', type=float, default=10**-3, help='Epsilon')
def optimization(type, func, first, second, third, iter, epsilon):
    if type not in allowed_methods:
        print('Invalid method')
        return
    if type == 'sec':
        if func is None or first is None or second is None:
            print('Missing arguments')
            return
        result = sv_utils.secant_primary(func, first, second, epsilon)
        print(result)
    elif type == 'newt':
        if func is None or first is None or iter is None:
            print('Missing arguments')
            return
        result = sv_utils.newton_primary(func, first, iter, epsilon)
        print(result)
    elif type == 'fib':
        if func is None or first is None or second is None or iter is None:
            print('Missing arguments')
            return
        result = sv_utils.fibonacci_primary(func, first, second, iter, epsilon)
        print(result)
    elif type == 'GS':
        if func is None or first is None or second is None or iter is None:
            print('Missing arguments')
            return
        result = sv_utils.golden_section_primary(func, first, second, iter, epsilon)
        print(result)
    elif type == 'DS':
        if func is None or first is None or second is None:
            print('Missing arguments')
            return
        result = mv_utils.downhill_simplex_primary(func, first, second)
        print(result)
    elif type == 'lagin':
        if func is None or first is None or second is None:
            print('Missing arguments')
            return
        x = [first, second, third] if third else [first, second]
        result = mv_utils.lagrange_interpolation_primary(func, x)
        print(result)
    elif type == 'ls':
        if func is None or first is None or second is None:
            print('Missing arguments')
            return
        result = mv_utils.least_squares_primary(func, first, second)
        print(result['x'])
    elif type == 'CG':
        if func is None or first is None or second is None or iter is None:
            print('Missing arguments')
            return
        result = mv_utils.cauchy_gradient_primary(func, first, second, iter)
        print(result)
    
if __name__ == "__main__":
    optimization()
