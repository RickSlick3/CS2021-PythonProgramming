# Notes from week 6 (Module 6)

# Abstract Data Types

# Linked List as an abstraction
# first() returns data sitting at the front/head
# rest() returns a linked list without the front/head

empty = "end of linked list"

def link(first, rest=empty):
    return [first, rest]

def first(s):
    return s[0]

def rest(s):
    return s[1]

def print_list(s):  # RECURSIVE
    print(first(s), end= " -> ")
    if rest(s) is not empty:
        print_list(rest(s))
    else:
        print("#")
        
def print_it(s):  # USING LOOPS
    print(first(s), end= " -> ")
    while rest(s) is not empty:
        s = rest(s)
        print(first(s), end = " -> ")
    print("#")

def len(s):
    if s == empty:
        return 0
    else:
        return 1 +  len(rest(s))
    
def getItem(s, i):
    assert (i <= len(s) and i >= 0)
    if i == 0:
        return first
    else:
        return getItem(rest(s), i-1)

def last(s):
    return getItem(s, len(s)-1)

def addatend(s, item):
    if s == empty:
        return link(item)
    else:
        return link(first(s), addatend(rest(s), item))
    
def rev(s):
    if s == empty:
        return empty
    else:
        return addatend(rev(rest(s)), first(s))
   
# ----- TESTING -----
test = link(2, link(3, link(4, link(5))))

print(test) # ugly version of the data type we are creating           
print_list(test) # a better looking version of the list 
print_it(test)

print(len(test))
print(getItem(test, 0))