import optparse
def parseCLI(type):
    parser = optparse.OptionParser()
    if(type == "newton-mv" or type == "hessian"):
        parser.add_option("-f", "--function", dest = "fnc", help = "To get the function(in terms of x and y) as a command line argument.\n *Enter the function in QUOTES*.\n Do not forget to format the function in a python style syntax.\n(For EX: x**2 - 2*y + 10 rather than x^2 - 2y + 10)")
    else:
        parser.add_option("-f", "--function", dest = "fnc", help = "To get the function(in terms of x and y) as a command line argument.\n *Enter the function in QUOTES*.\n Do not forget to format the function in a python style syntax.\n(For EX: x**2 - 2*y + 10 rather than x^2 - 2y + 10)")
        parser.add_option("-a", "--x1", dest = "x1", help = "The initial value of x1(integer is expected)")
        parser.add_option("-b", "--x2", dest = "x2", help = "The initial value of x2(integer is expected)")
        if(type == "cauchy" or type == "marquardt"):
            parser.add_option("-i", "--iterations", dest = "iter", help="Specify the number of iterations (expects an integer)")
        if(type == "li"):
            parser.add_option("-c", "--x3", dest = "x3", help = "The initial value of x3(integer is expected)")
    [options, args] = parser.parse_args()
    if options.fnc == None:
        return False
    return options, args