a={'a':10,'b':20}
b={'c':50,'d':80}
# res={**a,**b}
# print(res)
for key,value in b.items():
    a[key]=value
print(a)


a=['a','b','c']
b=[1,2,3]
tem={}
for x in range(len(a)):
    print(a[x],'==',x,'===',b[x])
    tem[a[x]]=b[x]
print(tem)


res={'a':10,'b':11,'c':12,'d':13}
for x,y in res.items():
    if y%2==0:
        res[x]=y*2
print(res)


l=['karimnagar','warangal','jagtial']
t={}
for x in l:
    t[x]=len(x)
print(t)


'Sep -19'
'to print max value with max method'
res={'a':100,'b':200,'c':300,'d':400}
temp=max(sorted(res.items()))     #max, min, sum
print(temp)

'to print max value without using max method'
res={'a':100,'b':200,'c':300,'d':400}
max=0
e=''
for x,y in res.items():
    if y>max:
        max=y
        e=x
print(e,"====",max)

'to convert keys to values and values to keys'
res={'a':100,'b':200,'c':300,'d':400}
tem={}
for keys,values in res.items():
    tem[values]=keys
print(tem)

'to print count for certain key'
res=[{'name':'soumya','dept':'cse'},
     {'name':'pavithra','dept':'cse'},
     {'name':'tina','dept':'it'},
     {'name':'riya','dept':'eee'},]
tem={}
for x in res:
    d=x['dept']
    if d not in tem:
        tem[d]=1
    else:
        tem[d]+=1
print(tem)


'sorted orerder for both keys and values'
res={'a':100,'b':800,'c':300,'d':400}
tem=dict(sorted(res.items(),key = lambda item:item[1]))
print(tem)

res={'a':100,'h':800,'c':300,'d':400}
tem=dict(sorted(res.items(),key = lambda item:item[0]))
print(tem)