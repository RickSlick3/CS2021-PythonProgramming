# Notes from week 2 (Module 2) 

# Functional Programming

# FP (Functional Programming) decomposes a problem into a set of functions. Ideally, functions only
#   take inputs and produce outputs, and don’t have any internal state that affects the output.

from operator import sub, add
print(add(3,2))
print(sub(3,2))

#   Formal provability - A theoretical benefit is that it’s easier to construct a mathematical 
#       proof that a functional program is correct. This is different from testing a program on 
#       numerous inputs and concluding that its output is usually correct, 
#   Modularity and Ease of debugging and testing .- Functional Programs are more modular and 
#       programs composed of small functions are easier to read and to check for errors. 
#   Composability  - Functional programs are often created by arranging existing functions in 
#       a new configuration and writing a few functions specialized for the current task.

# A Pure function - ONLY produces a return value (with no side effects) and always evaluates to the
#       same result, given the same argument value(s). 

def returnOne(x):
    return int(x/x)

print(returnOne(22))

# A Non-Pure function - may produce some side effects (like printing to the screen) and may not 
#       always evaluate to the same result, given the same argument values.

# A Higher Order Function is a function which takes other functions as arguments or returns a function (or both).

print(add(add(3,2), sub(3,2)))

def ADD(x, y, z):
    return add(x, (add(y, z)))

# Functions as arguments: Suppose we’d like evaluate a function on each natural number from 1 to n and print the result as we go. 

import math
def every(func, x):
    for element in range(1, x):
        print(func(element))        
every(math.sqrt, 5)

# Sometimes we wish to write a function so that given some set of arguments returns a function that 
#     will do something with those arguments when it is called. The key here is that your function 
#     is supposed to return a function and not evaluate anything yet. 

# A dispatch function gives a programmer the flexibility to use a single named function to operate 
#     differently based on single special argument, which we call an option. Each option is 
#     associated with a different function used to process the values(s). The following simple 
#     example shows how a dispatch function can be created with 2 options (associated with 2 functions).
#     This dispatch function is created using a higher-order function that registers the 
#     associations and returns the dispatch function.

# How to define a function. Function definitions consist of a def statement that indicates a <name> 
#     and a comma-separated list of named <formal parameters>, then a return statement, called the 
#     function body, that specifies the <return expression> of the function, which is an expression
#     to be evaluated whenever the function is applied:
    
def NAME_HERE(PARAMETERS):
    return 0    # replace with an expression

# Control statements are statements that control the flow of a program's execution based on the results of logical comparisons.

# Assertions. Programmers use assert statements to verify expectations, such as the output of a 
#     function being tested. An assert statement has an expression in a boolean context, followed 
#     by a quoted line of text (single or double quotes are both fine, but be consistent) that will 
#     be displayed if the expression evaluates to a false value.

def add(x, y):
    return x + y
    
assert add(2, 1) == 3, 'This should be 3'
assert add(11, 11) == 22, 'This should be 22'
assert add(50, 0) == 50, 'This should be 50'

# Doctests. Python provides a convenient method for placing simple tests directly in the docstring 
#     of a function. The first line of a docstring should contain a one-line description of the 
#     function, followed by a blank line. A detailed description of arguments and behavior may 
#     follow. In addition, the docstring may include a sample interactive session that calls the function:

