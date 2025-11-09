"while loop"
x=0
while(x<21):
    print(x)
    x+=1

x=123
t=0
while x>0:
    s=x%10
    t+=s
    x//=10
print(t)

x=123
t=0
while x>0:
    s=x%10
    t=t*10+s
    x//=10
print(t)

x=127
tem=x
t=0
while x>0:
    s=x%10
    t=t*10+s
    x//=10
if tem==t:
    print("palindromre")
else:
    print("not a palindrome")

while True:
    text=input("Enter something (type 'exit' to stop): ")
    if text=="exit":
        break

x=4
fact=1
while x>0:
     fact*=x
     x-=1
print(fact)

n=10
a,b=0,1
cou=0
while cou<n:
    print(a)
    a,b=b,a+b
    cou+=1

num=123456
cou=0
while num>0:
    cou+=1
    num//=10
print(cou)

import random
while True:
    n=random.randint(1, 100)
    print(n)
    if n%7==0:
        break
