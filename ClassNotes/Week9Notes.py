# Linked List example

class Link:
  empty = 'empty'

  def __init__(self, first, rest=empty):
    self.first = first
    self.rest = rest

  def __len__(self):
    if self.rest == Link.empty:
      return 1
    else:
      return 1 + len(self.rest)

  def __getitem__(self, index):
    if index == 0:
      return self.first
    else:
      return self.rest[index-1]
 
  def __repr__(self):
    if self.rest == Link.empty:
      repstr = ''
    else:
      repstr=", " + Link.__repr__(self.rest)
    return 'Link({0}{1})'.format(self.first, repstr)

  def __gt__(self, other):
    return len(self) > len(other)   
  
  def __add__(self, other):
    if self == Link.empty:
      return other
    else:
      return Link(self.first, Link.__add__(self.rest, other))
  

  def __call__(self,f):
    if self == Link.empty:
      return self
    
    if self.rest == Link.empty:
      self.first = f(self.first)
      return self
    
    self.first = f(self.first)
    self.rest.__call__(f)
    return self

def map_shallow(f, lst):
  if lst == Link.empty:
    return lst
  else:
    return Link(f(lst.first), map_shallow(f,lst.rest))

x = Link(1, Link(2))
y = Link(3, Link(4, Link(5)))
z = x + y
print(x, " + ")
print(y, " = ")
print(z)
print(map_shallow(lambda i: i*i,z))
y(lambda i: i*10)
print(y)