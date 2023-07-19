# Notes from week 5 (Module 5)

# -----Dictionaries-----

d = {} # dictionary declaration

print(type(d)) # Outputs the primitive type of the argument

d = {'one': 'uno', 'two': 'dos'} # defines d
print(d['two']) # returns definition of two

# d = d + {'three':'tres'} causes an error because of the '+' operator
d['three'] = 'tres!' # adds a new key
d['three'] = ['tres1', 'tres2'] # changes def of three by making it a list

d[(1, 2)] = "test" # can make a touple a key, but CANNOT use a list
print(d)

d['four'] = d['one'] * 2 # makes the new entry multiplied by 2
print(d)

print(len(d))

# -----Histogram Example-----
def histogram(seq):
    freqtable = {}
    for x in seq:
        if x not in freqtable:
            freqtable[x] = 1
        else: 
            freqtable[x] += 1
    return freqtable

#testing examples
t = histogram("roberto")
print(t)
s = "to be or not to be"
sh = histogram(s)
print(sh)

sh = histogram(s.split()) # splits a string into words 
print(sh) 


# -----Bigger Example-----
url = "https://www.gutenberg.org/files/1533/1533-0.txt"
import os
from urllib.request import urlopen
shakes = urlopen(url)
shakestoken = shakes = shakes.read().decode('utf-8').split()

shtable = histogram(shakestoken[10100:10200]) #uses a sliced list of 100 words
print(shtable)

print(shtable['the']) # how many times the word appeared
del(shtable['the']) # deletes the word from the histogram


# -----Successor Example-----
def s_table(seq):
    table = {}
    for x in seq:
        table[x] = []
    prev = seq[0]
    for x in seq[1:]:
        if x not in table[prev]:
            table[prev] += [x]
        prev = x
    return table

q = "to be or not to be"
qtable = s_table(q.split())
print(qtable)