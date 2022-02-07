import numpy as np
from scipy.interpolate import lagrange
from cli_mv import parseCLI


res = parseCLI(type = "li")
if res == False:
    print("No inputs provided....")
else:
    [options, args] = res
    fnc = str(options.fnc)
    a = int(options.x1)
    b = int(options.x2)
    c = int(options.x3 or 0)
    if c == 0:
        x = np.array([a,b])
    else:
        x = np.array([a, b, c])

y = eval(fnc)

poly = lagrange(x, y)
print(poly)