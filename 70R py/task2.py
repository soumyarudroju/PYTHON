a=17
print(a//7,a%7)


total=0
for i in range(1,6):
    total+=i
print(total)    


print(12&5)


num=13
print(num&1)


list1=[10,20]
list2=[10,20]
print(list1 is list2)

fruits=["apple","banana","cherry"]
print("mango" in fruits)

a=5
a*=3
print(a)

print(2**3**2)

a=10
a-=3
print(a)

x=True
y=False
print(x and not y)

print(6|3)

name="PYTHON"
print("Y" in name and "Z" not in name)

a=8
b=2
a//=b
print(a)

list=["a","b"]
list2=list1
print(list1 is list2)

a=1
b=3
a=a^b
b=a^b
a=a^b
print(a,b)