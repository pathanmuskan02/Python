# Lists 

lst = []
lst1 = list()
print(type(lst),type(lst1))

# append(element)
lst.append(10)
print(lst)

lst.append(20)
lst.append(30)
lst.append(40)
lst.append(50)
print(lst)
lst.append([1,2,3])
print(lst)

# extend(multiple elements)
lst.extend([1,2,3,4])
print(lst)

# insert(position,element)
lst.insert(0,100)
print(lst)

# removing element from the list
# remove(element)
lst.remove(100)
print(lst)

# checking if element present in list and removing
element = 100
if element in lst:
    lst.remove(element)
print("No Element")

# difference b/w sort and sorted
l = [7,5,8,912,2,1,6]
print(l)
# l.sort()
# print(l)
l2 = sorted(l)
print(l2)
