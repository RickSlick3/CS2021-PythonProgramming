# Notes from week 1 (Module 1)

# Basics

# The Python Interpreter - a program that reads and runs you code line by line

#   “>>>” is the default prompt line. 
#   Ending your line with “:” lets you indent without entering the code. 
#   “help” allows you to pull up docs and definitions of each function

# Python IDEs: There are many Integrated Development Environments and Package Management Systems
#   for Python Programming including IDLE, PyCharm, VSCode. 

# PACKAGE TERMINOLOGY 

#   Programs are composed of modules, Libraries are packages of modules, modules contain statements, 
#   statements contain expressions, expressions create and process objects.

# When Programming:
  
#   Test incrementally: Try out everything you write as soon as possible to identify problems 
#       early and gain confidence in your components. 
#   Isolate errors: When trying to diagnose a problem, trace the error to the smallest fragment 
#       of code you can before trying to correct it. 
#   Check your assumptions: Know your assumptions, then focus your debugging effort on verifying 
#       that your assumptions hold. 
#   Consult others: If you don't understand an error message, ask a friend, instructor, or 
#       search engine. If you have isolated an error, but can't figure out how to correct it, ask 
#       someone else to look. A lot of valuable programming knowledge is shared in the process
#       of group problem solving.

# Docstrings in Python are string literals that occurs as the first statement in a module, 
#   function, class, or method definition. Such a docstring becomes the __doc__ special 
#   attribute of that object. 

# The doctest module: There is a standard python module called “doctest” that is useful for 
#   setting up a TDD testing framework. The doctest module searches for pieces of text that 
#   look like interactive Python sessions inside of the documentation parts of a module, and then
#   executes (or executes) the commands of those sessions to verify that they work exactly as 
#   shown, i.e. that the same results can be achieved. In other words: The comments or help text 
#   of the module is parsed and run through the python interpreter sessions. These slices of 
#   example code are run, and the results are compared against expected values indicated in the tests. 

# DOCTEST EXAMPLE 
def add(x, y):
    """ adds x and y and returns the value
    >>> add(5, 10)
    15
    >>> add(1, 1)
    2
    """
    return x + y

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)

# Usage of doctests: To use the “doctest module” it has to be first imported. The part of an 
#   interactive sessions with the example test code and the associated expected outputs must 
#   be copied inside of the docstring of the corresponding function.

# Modules: a block of code imported by some other code. 

#   Three types of modules concern us here: pure Python modules, extension modules, and packages.
#       A module written in Python and contained in a single .py file is sometimes referred to
#       as a “pure module.” An extension module may be written in the low-level language (e.g. C) 
#       of the Python implementation 

# A package is a special module that contains other modules; typically contained in a directory 
#   in the filesystem and distinguished from other directories by the presence of a file named __init__.py. 

# Using the Module System - import and from: Clients of module (.py file) that use import get a 
#   module with attributes, while clients that use from get copies of the file’s names. Generally,
#   you will prefer to use import. Python programs are composed of multiple module files linked 
#   together by import statements, and each module has attributes -- a collection of variable 
#   names—usually called a namespace.

# Installing and Running Python Libraries: The Power of Python is in its large standard library 
#   and the availability of 3rd Party Packages. Python has several alternatives for installing 
#   3rd party packages. Since we will mostly be using the web application repl.it, many of the 
#   configuration issues will be handled by that system. 





