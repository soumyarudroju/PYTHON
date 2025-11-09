"list comprehension"
s=[x*x for x in range(1,21)]
print(s)

s=[x for x in range(1,51) if x%2==0]
print(s)

l=['apple','banana','owl','icecream']
s=[x for x in l if x.startswith('AEIOUaeiou')]
print(s)

mat=[[1,2,3],[6,5],[7,8,9]]
r=[j for x in mat for j in x]
print(r)

s=[x for x in range(1,51) if all(x%y!=0 for y in range(2,x))]
print(s)

s=[x for x in range(1,101) if x%3==0 and x%5==0]
print(s)


print(s)

s=[(x,x*x) for x in range(1,16)]
print(s)

l=[1,-8,5,-9,4,6,-7,-3]
s=[x for x in l if x<0]
print(s)
