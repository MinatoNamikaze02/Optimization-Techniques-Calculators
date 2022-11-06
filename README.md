# Optimization-Techniques-Calculator
## Overview 
   A simple CLI application that can calculate the following optimization techniques:
   - Newton Raphson
   - Secant Method
   - Fibonacci Search
   - Golden Section Search
   - Cauchy Gradient
   - Lagrange Interpolation
   - Least Squares
   - Downhill Simplex
   **More to come**

## Why we did this?
   We like math! 🤓

## How to use this
   * Clone this repository.
   * Run `pip install -r requirements.txt`.
   * Run the main with relevant options and arguments.

## Options and Arguments
```
Arguments
type                       The value that specifies the optimization problem type
Accepted Types:
             SECANT                   'sec'
             NEWTON                   'newt'
             FIBONACCI                'fib'
             GOLDEN SECTION           'GS'
             DOWNHILL SIMPLEX         'DS'
             LAGRANGE INTERPOLATION   'lagin'
             LEAST SQUARE             'ls'
             CAUCHY GRADIENT          'CG'
Options:
  -f, --func TEXT           Function to be optimized (Enter the function in python style syntax).
  -x1, --first FLOAT        Leftmost of an interval (or) initial guess
  -x2, --second FLOAT       Rightmost of an interval
  -x3, --third FLOAT        Third value of x (applies only for lagrange interpolation)
  -i, --iter INTEGER        Number of iterations
  -e, --epsilon FLOAT       Epsilon (by default 10^-3)
  --help                    Shows the help message
```

## Examples
```
$ python3 main.py newt -f "x**2 - 2" -x1 1 -i 10
```
```
>>> 1.414213562373095
```
 
## Side Notes
   * It's not necessary for you to know the concepts to use these calculators, however it is recommended that you do.
   * This calculator was tested with various questions and the answers were pretty accurate (a lot of anomolies are to be expected).
   * Enter the function in python style syntax (eg: `x**2 + 2*x + 3` instead of `x^2 + 2x + 3`).
   
## Getting a wrong answer?
   * Re-check your input function (the syntax expected is slightly different -> [updates](#Updates)).
   * Check the input values you've fed. 
   * If you function string has spaces, try enclosing it in quotes.
   * See if your answer was obtained a few iterations prior.

## Updates
   * Moved to [click](https://www.google.com/search?client=safari&rls=en&q=click+python&ie=UTF-8&oe=UTF-8) for better CLI experience.

## How can you help?
- Feel free to open issues/PR's for any bugs or improvements.
- If you have any suggestions (new methods) feel free to open an issue regarding that!
