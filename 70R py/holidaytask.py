"list comprehension"
s=[x*x for x in range(1,21)]
print(s)

s=[x for x in range(1,51) if x%2==0]
print(s)

l=['apple','banana','owl','icecream']
s=[x for x in l if x.startswith('AEIOUaeiou')]
print(s)

l=[85,65,72,95]
s=[x for x in l if ]

mat=[[1,2,3],[6,5],[7,8,9]]
r=[j for x in mat for j in x]
print(r)

s=[x for x in range(1,51) if all(x%y!=0 for y in range(2,x))]
print(s)

s=[x for x in range(1,101) if x%3==0 and x%5==0]
print(s)

l=['apple','banana','owl','icecream']
s=[x for x in l x.rev]

s=[(x,x*x) for x in range(1,16)]
print(s)

l=[1,-8,5,-9,4,6,-7,-3]
s=[x for x in l if x<0]
print(s)
"string"
s='soumya'

"dictionary comprehension"
"for loop"
for x in range(1,51):
    print(x)

n=7
for x in range(1,11):
     print(n*x)

n=10
for x in range(1,n+1):
    if n%x==0:
        print(x)

s="python"
cou=0
for x in s:
    if x in "aeiou":
        cou+=1
        print(x)
print(cou)

l=[10,31,12,42,23]
num=l[0]
for x in l:
    if x > num:
        num=x
print(num)

a,b=0,1
for x in range(1,11): 
    print(a) 
    a,b=b,a+b 

s='python'
t=""
for x in s:
    t=x+t
print(t)

sen="python is easy to learn"
cou=1
for x in sen:
    if x == " ":
        cou+=1
print(cou)

for x in range(2,101):
    for y in range(2,x):
        if x % y==0:
            break
    else:
        print(x, end=" ")

l=[[10,20,20],
   [40,50],
   [60,70]]
for x in l:
    for y in x:
        print(y, end=" ")
    print()

l=[10,11,12,14,15,17,18]
for x in l:
    if x%2==0 and x%3==0:
        print(x)

l=['python','java','c++']
t=l[0]
for x in l:
    if len(x)>len(t):
        t=x
print(t)

l=[123, 45, 789]
t=0
for x in l:
    for y in str(x):
        t+=int(y)
    print(t)

s = "ABC"
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])
   
for i in range(1,1001):
    b=0
    for j in range(1,i):
        if i%j==0:
             b+=j  
    if b==i:        
        print(i)

sen="Python is fun"
word=sen.split()
for x in word:
    print(x[::-1], end=" ")

