# Sets and Dictionaries
# Sets
s = {1,2,3,5}
s1 = set()
s2 = {}
print(type(s),type(s1),type(s2))

# add(element)
s.add(10)
print(s)

# remove(element)
s.remove(10)
print(s)

# discard(element)
s.discard(5)
print(s)

s.discard(100)
print(s)

# Set Operations
s1 = {10,20,30,40}
s2 = {40,50,60}
print(s1)
print(s2)
# union()
print(s1.union(s2))
print(s1 | s2)
# Intersection
print(s1.intersection(s2))
print(s1 & s2)
# Difference
print(s1.difference(s2))
print(s1 - s2)
print(s2.difference(s1))
print(s2 - s1)
# Symmetric Diffrence
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

# is super set and is sub set
s3 = {26,45,18,1,4}
s4 = {26}
# issuperset
print(s3.issuperset(s4))
# issubset
print(s3.issubset(s4))
print(s4.issubset(s3))

# Dictionaries
d = {}
d1 = dict()
d2 = {'a':1,
      'b':2,
      'c':3}
print(type(d),type(d1),type(d2))

print(d2['a']) # to get value in a

print(d2.values())
print(d2.keys())
print(d2.items())

# to assign new value to c key
d2['c'] = 6
print(d2)

# to add new value
d2['d'] = 4
print(d2)

# Assigning value using update
d2.update({'e':5})
print(d2)
   # or
d2.update(f=6)
print(d2)

# print using get operation
print(d2.get('c'))
print(d2.get('z',0)) # print z key value in d2 ,if z not there in d2 print 0
print(d2.get('a',0)) # a is there so it will print value of a

# removing using pop
d2.pop('b')
print(d2)
d2.pop('b',None) # if b present it will pop otherwise none

d2.popitem()
print(d2)

del d2
print(d2)

d2.clear()
print(d2)