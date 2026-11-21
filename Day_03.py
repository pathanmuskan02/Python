# Operators
x = 10
y=100
print(x+y,x-y,x*y,x/y,x//y,x%y,x**y)

# Assignment Operator
x = 200
print(x)
x+=100    # x = x+100
print(x)
x-=200
print(x)
x*=4
print(x)
x//=2
print(x)
x%=2
print(x)

# Relational Operator
x = 26
y = 14
print(x<y,x>y,x==y,x!=y,x>=y,x<=y)

# LOgical Operators
print((x<y) and (x==y))
print((x>y) and (x!=y))
print((x<y) or (x>=y))
print(not (x<y))
print(not (x>y))

# Bitwise Operators
n1 = 45
n2 = 4
print(n1 & n2)
print(n1 | n2)
print(n1 ^ n2)
print(~n2)
print(n2 << 2)
print(n2 >> 1)

# Membership Opertaor
l = [10,2,3,4,5]
print(100 not in l)
print(4 in l)
print(5 not in l)

# Identity Operator 
x = 5
y = 5
print(x is y)
a = [1,2,3]
b = a
print(a is b)

# You bought 3 items costing a, b, and c. Find the total amount to pay.
a = int(input("cost of first item: "))
b = int(input("cost of second item: "))
c = int(input("cost of third item: "))
total = a + b + c
print("Total amount =", total)

# Check whether three sides can form a triangle
# a + b > c
# a + c > b
# b + c > a
a = int(input("first side: "))
b = int(input("second side: "))
c = int(input("third side: "))
if a + b > c and a + c > b and b + c > a:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")

# Convert minutes into seconds
# Seconds = Minutes × 60
minutes = int(input("minutes: "))
seconds = minutes * 60
print("Seconds =", seconds)