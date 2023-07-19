# Notes from week 3 (Module 3)

# Recursion

# A Recursive function is one that can call itself before it returns. 
# Evaluating a call to a recursive function is not essentially different from evaluating a non-recursive function. 
# It is easy to misuse recursion and potentially get into an infinite loop. 

# Python interpreters set a fixed limit on how many times one function can call itself. 
# We can get the current limit and even reset that limit using a module called sys.

import sys
print(sys.getrecursionlimit()) # typical default is 1000
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

# A recursive function is a function that calls itself in its body, either directly or indirectly. Recursive functions have three important components:

#   Base case(s), the simplest possible form of the problem you're trying to solve.
#   Consider a recursive call on a smaller argument.
#   Recursive case(s), where the function calls itself with a simpler argument as part of the computation.

# EXAMPLE^^^
def fib(n):
    # BASE CASE
    if n == 1:
        return 0
    # SMALLER ARGUMENT
    if n == 2:
        return 1
    # RECURSIVE CASE(S)
    else:
	    return fib(n-2) + fib(n-1)
	
result = fib(6)

# How to count up and down with recursion:
def countup(n):
    if n == 0:
        print(0)
    else:
        countup(n-1) # calls the function again
        print(n) 
def countdown(n):
    if n == 0:
        print(0)
    else:
        print(n)
        countdown(n-1) # calls the function again
        
countup(5)
countdown(5)

# Each recursive call extends the current environment adding at least the binding of the arguments in the call. 
  
#   Suppose that we are to evaluate fib(2) under some environment ENV0, you may think of ENV0 as 
#   the default global environment. Given that 2 is already a value, we extend ENV0 to ENV1 with
#   a binding between n and 2 and start to evaluate the body of fib under ENV1; clearly, this 
#   evaluation leads to the evaluation of fib(n-1) + fib(n-2); it is easy to see that evaluating 
#   fib(n-1) and fib(n-2) under ENV1 leads to 1 and 0, respectively, and the evaluation of 
#   fib(n-1) + fib(n-2) eventually returns 1 (as the result of 1+0); thus the evaluation of fib(2)
#   under ENV0 yields the integer value 1. 

#   Let us now evaluate fib(3) under ENV0; we extend ENV0 to ENV2 with a binding between n and 3, 
#   and start to evaluate the body of fib under ENV2; we then reach the evaluation of 
#   fib(n-1) + fib(n-2) under ENV2; evaluating fib(n-1) under ENV2 leads to the evaluation of 
#   fib(2) under ENV2, which eventually returns 1; evaluating fib(n-2) under ENV2 leads to the 
#   evaluation of fib(1) under ENV2, which eventually returns 1; therefore, evaluating fib(3) 
#   under ENV0 returns 2 (as the result of 1+1). 

# EXAMPLE:
def sumdigits(n):
    """
    >>>sumdigits(134)
    8
    >>> sumdigits(5679)
    27
    """
    if n < 10:
       return n
    else:
        last = n % 10
        prefix = n //10
        return last + sumdigits(prefix)
    
print(sumdigits(135))

# When a recursive procedure is divided among two functions that call each other, 
#   the functions are said to be mutually recursive. 

def is_even(n):
    if n == 0:
        return True
    else:
	    return is_odd(n-1)
	
def is_odd(n):	    
    if n == 0:
        return False
    else:
        return is_even(n-1)
	
result = is_even(4)
print(result)

# Another common pattern of computation is called tree recursion, in which a function calls itself more than once.
