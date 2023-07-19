# Notes from week 8 (Module 8)

# Trees

# defined recursively, 

# Operations
#   Constructor - tree()
#   Accessor - root(), branch()
#   Add Branch - add_branch()
#   Check base case - is_leaf() checks no branches

# example tree:
def tree(root_obj, branches=[]):
    return [root_obj] + list(branches)

def root(t):
    return t[0]

def branches(t):
    return t[1:0]

def is_leaf(t):
    # return len(t) == 1
    # return branches(t) == []
    return not branches(t)

def add_branch(t, x):
    return tree(root(t), branches(t) + [tree(x)])

def add_all(t):
    if is_leaf(t):
        return root(t)
    else:
        sumb = 0
        for b in branches(t):
            sumb += add_all(b)
        return root(t) + sumb
    
def add_all_one_line(t):
    return root(t) + sum([add_all_one_line(b) for b in branches(t)])

def fibtree(n):
    if n == 1 or n == 0:
        return tree(1)
    else:
        t1 = fibtree(n-1); t2 = fibtree(n-2)
        return tree(root(t1) + root(t2), [t1] + [t2])
    
from random import randint
def random_walk(t):
    if is_leaf(t):
        print("visit leaf ", root(t))
    else:
        print("Visit ", root(t))
        i = randint(0,1)
        random_walk(branches(t)[i])

