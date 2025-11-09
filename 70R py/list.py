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

s=[(x,x*x) for x in range(1,16)]
print(s)

l=[1,-8,5,-9,4,6,-7,-3]
s=[x for x in l if x<0]
print(s)


'Write a list comprehension in Python that checks whether each number in a given list is "prime" or "not prime" and returns the result as a list.'
n=[11,25,85,45]
s=['prime' if all(x%y!=0 for y in range(2,x))  else 'not prime' for x in n]
print(s)

'Using list comprehension, generate a 2D list with the following structure'
'input=[[1,2,3],[4,5,6],[7,8,9]] ==> output=[[1, 4, 7], [2, 5, 8], [3, 6, 9]]'
r=[[1,2,3],[4,5,6],[7,8,9]]
res=[[x[y]for x in r] for y in range(len(r[0]))]
print(res)

'Using list comprehension, generate a list of tuples mapping ASCII values to characters for uppercase letters A, B, C.'
r=['A','B','C','a']
s=tuple((x,ord(x)) for x in r if x.isupper())
print(s)
