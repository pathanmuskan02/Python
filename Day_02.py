#Numeric Data types
number = 120
percentage = 8.0
a = 4+5j
print(number,type(percentage))
print(percentage)
print(a,type(a))

#Sequence Data types
s = "Muskan"
lst = [10,20,30]
t=(10,20,30)
print(type(s),type(lst),type(t))

#Boolean Data types
#True/False
boole = True
print(type(boole))
print(boole)

boole1 = True
boole2 = False
print(boole1 + boole2)

#Mapping Data type - Dictionary
d = {"name":"codegnan",
     "Location":"Hyd",
     "Branch":4}
print(d,type(d))

#sets
s = {1,2,3,4}
print(type(s))

#Empty list,tuple,string,dictionary,set
lst1 = []  #list()
t1 = ()    #tuple()
str1 = ""  #str()
d1={}      #dict()
s1=set()
print(lst1,type(lst1))
print(t1,type(t1))
print(str1,type(str1))
print(d1,type(d1))
print(s1,type(s1))

#Explicit type casting - type conversion
n = input()
print(type(n))
n2 = int(n)
print(type(n2))

#Implicit type casting - type conversion
n1 = 12
n2 = 3.5
n3 = n1 + n2
print(n3,type(n3))

str1 = "Muuskaan"
print(str1)
lst2 = list(str1)
print(lst2)
t2= tuple(lst2)
print(t2)
set2 = set(lst2)
print(set2)

#input from user 
num = int(input())
s = input()
list1 = list(map(int,input().split(",")))
tuple1 = tuple(map(int,input().split()))
set1 = set(map(int,input().split()))
print(num)
print(s)
print(list1)
print(tuple1)
print(set1)