# Conditional Statements
# Simple if or if
age = int(input())
if age>=18:
    print("Eligible for Voting")

# if else
age = int(input())
if age>=18:
    print("Eligible for Voting")
else:
    print("Not Eligible")

# check whether given num even or odd
num = int(input())
if num%2==0:
    print("even")
else:
    print("odd")

# check whether given num +ve or -ve
num = int(input())
if num>0:
    print("positive")
else:
    print("negetive")

# if elif
marks = int(input())
if marks>=35 and marks<50:
    print("D grade")
elif marks>=50 and marks<75:
    print("C grade")
elif marks>=75 and marks<90:
    print("B grade")
elif marks>=90:
    print("A grade")

# Fizz Buzz
num = int(input())
if num%3==0 and num%5==0:
    print("Fizz Buzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")

# Nested if
# greatest among 3 numbers
'''a = int(input())
b = int(input())
c = int(input())'''
a,b,c = map(int,input().split()) # Taking 3 inputs in same line
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b<c:
        print(b)
    else:
        print(c)

# Nested if using elif
a,b,c = map(int,input().split())
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)

# Nested if using elif (if input negetive or positive)
a,b,c = map(int,input().split())
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
elif c >= a and c >= b:
    print(c)