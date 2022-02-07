import optparse
def parseCLI(type="secant"):
    parser = optparse.OptionParser()
    parser.add_option("-f", "--function", dest = "fnc", help = "To get the function(in terms of x) as a command line argument.\n *Enter the function in QUOTES*.\n Do not forget to format the function in a python style syntax.\n(For EX: x**2 - 2*x + 10 rather than x^2 - 2x + 10)")
    parser.add_option("-e", "--epsilon", dest = "E2", help = "The value of epsilon either in python style syntax or as a floating value is expected. (For EX: 10**-3 or 0.001) *Default value is 0.001*")
    parser.add_option("-a", "--x1", dest = "x1", help = "The initial value of x1(integer is expected)")
    parser.add_option("-b", "--x2", dest = "x2", help = "The initial value of x2(integer is expected)")
    if(type == "fib" or type == "GS" or type == "newt"):
        parser.add_option("-i", "--iterations", dest = "iter", help="Specify the number of iterations (expects an integer)")
    [options, args] = parser.parse_args()
    if options.fnc == None:
        return False
    return options, args