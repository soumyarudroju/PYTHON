for i in range(1,11):
    print(i)

for i in range(2,21,2):
    print(i)

for i in range(1,20,2):
    print(i)

for i in range(10,0,-1):
    print(i)

for i in range(1,11):
    print(i,"squared no:",i*i)

num=5
for i in range(1,11):
    print(i,"table:",num*i)

total=0
for i in range(1,101):
    total+=i
    print("sum:",total)

product=1
for i in range(1,11):
    product*=i
    print("factorial of 10",product)

for i in range(1,51):
    if i%5==0:
        print(i)

for i in range(1,31):
    if (i%2==0 and i%3==0):
        print(i)

n=5
for i in range(1,n*2,2):
    print("first",n,"odd numbers are:",i)
    print(end="")

n=5
for i in range(0,n*2,2):
    print("first",n,"even no are:",i)

n=10
for i in range(10,0,-1):
    print("numbers from",n,"down to 1",i)

n=10
for i in range(1,n,2):
    print("numbers from 1 to",n,"in steps of 2",i)

n=10
for i in range(1,n,3):
    print("numbers from 1 to",n,"in steps of 3",i)

n=10
square=0
for i in range(1,n):
    square+=i**2
    print(i,"sum of squares:",i*i)

n=10
cube=0
for i in range(1,n):
    cube+=i**3
    print(i,"sum of cubes:",i*i*i)

n=5
product=1
for i in range(1,n+1):
    product*=i
    print("the product of first",n,"natural numbers are:",product)

n=20
for i in range(5,n,10):
    print(" the numbers between 1 and",n,"that end with digit 5 are:",i)

n=10
count=n//4
print("numbers between 1 and",n,"are divisible by 4:",count)

n=10
count=n-(n//2)
print("numbers between 1 and",n,"are not divisible by 2:",count)

n=10
for i in range(2,n,2):
    print("the square of only even numbers between 1 and",n,"are:",i*i)

n=10
for i in range(1,n,2):
    print("the cube of only odd numbers between 1 and",n,"are:",i*i*i)

n=10
for i in range(1,n):
    if i%2==0 and i%3==0:
        print("all numbers between 1 and",n,"that are divisible by both 2 and 3 are:",i)

n=10
for i in range(1,n):
    if i%2==0 or i%5==0:
        print("all numbers between 1 and",n,"that are divisible by both 2 and 5 are:",i)

n=15
for i in range(1,n):
    if i%7==0:
        print("the sum of numbers between 1 and",n,"that are divisible by 7 are:",i)

n=10
total=0
for i in range(1,n+1):
    if i%3 !=0:
        total+=i
        print("the sum of numbers between 1 and",n,"that are not divisible by 3 are:",total)

