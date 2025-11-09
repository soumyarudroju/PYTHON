list=[10,20,30,40,50]
print(list)
print(list[2])
list.insert(2,60)
print(list)
list.append(70)
print(list)
list.insert(1,80)
print(list)
list.remove(80)
print(list)
list.pop(3)
print(list)
print(len(list))
if 20 in list:
    print("yes element exists in the list")
for i in list:
    print(i)
list.sort()
print("ascending order",list)
list.sort(reverse=True)
print("descending order",list)
list1=[50,60,70,80]
list1.reverse()
print("revese list is",list1)
list2=[30,40,50]
print(list2[::-1])
a=[10,20]
b=a.copy()
print(b)
original_list=[1,2,3,4,5]
copied_list=original_list[:]
print("original_list",original_list)
print("copied_list",copied_list)
l=[10,20,30,40,10,50,10]
l.clear()
print(l)

num=[1,2,2,3,3,4,2]
print(num.count(2))
print(num.index(4))
c=[10,20,30,40,50]
d=[60,70,80,90,100]
print(c+d)
print(c*3)
print(c[1:5:2])
print(c[2:5])
numbers=[2,3,12,15,18]
if all(i>0 for i in numbers):
    print("all elements are positive")
else:
    print("not all elements are positive")
list5=[10,20,30,40,50]
r=str(list5)
print(r)
print(type(r))
print(max(list5))
print(min(list5))
print(sum(list5))
for i in list5:
    print(i*i)

number = [1,2,3,4,5,6,7,8,9]
count=[]
for i in number:
    if i%2==0:
        count.append(i)
print(count)
number = [1,2,3,4,5,6,7,8,9]
count=[]
for i in number:
    if i%2!=0:
        count.append(i)
print(count)

lis=[1,2,3,2,3,4,5,6,2]
print(set(lis))
my_list=[1,2,3,4,4,5,6,3,2,4]
unique_list = set(my_list)
print(unique_list)
uni_list=[1,12,12,3,12,3,3,12,3]
res=set(uni_list)
print("unique elements",res)
empty_list=[]
if len(empty_list)==0:
    print("empty list")
else:
    print("not empty list")
n=5
zeros =[0]*n
print(zeros)
num = [10,20,30,40]
num[0],num[1]=num[1],num[0]
print(num)
list = [10,20,30,40,50]
print(list[-1])