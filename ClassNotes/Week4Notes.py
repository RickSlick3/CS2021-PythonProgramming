# Notes from week 4 (Module 4)

# Lists and Sequences

# List look like: 
digits = [0, 1, 2, 3]

# All normal operators can be use on lists (+, *)
digits += [4]
digits += [5, 6, 7]
digits = digits * 2

# deleting
x = digits.pop(0) # x = digits[0]
digits.delete[0] # deletes index 0
digits.remove(0) # removes any 0 in digits

# Membership: use the “in” or “not in” to find if a value is in a list
if 1 in digits: 
    print("1 is in digits")
if 10 not in digits:
    print("10 is not in digits")
  
# Slicing gets a sub list from a whole list: 
print(digits[0:4])  # inclusive:non-inclusive
digits[:4] # first 4 digits
digits[3:] # all digits after first number

# Length: 
print(len(digits))

# Access:
index = 3 
digits[index] # gets the item at index 3
digits[-1] # gets the last item in the list

# Multiple Elements: 
pairs = [[1, 2], [3, 4]]

# Access: 
pairs[0] # [1, 2]
pairs[1][1] # 4


# Iteration: 
#   Use “_” to represent nothing
x = 1
y = 4
while x < y:
    x += 1

for element in digits:
    print(element)
    
for x, y in pairs:
    x += 2
    y += 5
print(pairs)

# Ranges: range(num1, num2)  range(1, 10)  #(inclusive, exclusive)
for i in range(1, 10):
    x += 5 # or some other expression

# List Comprehension: [“expression” for “name” in “list” if “expression”]
[x*5 for x in digits if x%2 == 0]
print(digits)

# Mapping: applies a function to all elements in a sequence
def map(func, seq):
    new = []
    for item in seq:
        new += [func(item)]
    return new

s = lambda x: (x*x)
map(s, [1,2,3]) # squares every number in the sequence

# filter: only returns the result if it passes the predicate
def filter(pred, seq):
    new = []
    for item in seq:
        if pred(item):
            new += [item]
    return new

h = lambda x: x%2 == 0
filter(h, [1,2,3]) # only returns numbers divisible by 2

# from functools import reduce: reducing is taking all input and accumulating into a single value

# from operator import mul???
 
# Multiline Strings: use “ “ “string” “ “ or “\n”

# Use str() to do a type conversion

# Strings can use the “len(x)”, “[x]”, “in” and “not in”, as well as normal operators

