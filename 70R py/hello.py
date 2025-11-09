#DAY-2
#a=0x1234567af
#print(a)
#print(type(a))
#print(id(a))

#a=0o1234567
#print(a)
#print(type(a))
#print(id(a))


#DAY-3

#string
#g='name'
#a='234'
#a='''Hello
#    Welcome'''
#print(a)

#swap
#a=1
#b=2
#a,b=b,a
#print(a)
#print(b)

#float
#f=12.3
#a=2e1 #e=10
#print(a)
#b=4E1
#print(b)

#BOOL
#p1=9
#p2=10
#res1=p1>p2
#res2=p2>p1
#print(res1)
#print(res2)

#print(int(True))
#print(int(False))

#index value variable name[] location of the character in the brackets

'DAY-4'

#print(int(True+True))
#print(int(False+False))

#"complex ==> imaginary+real"
#v=2+3j
#print(type(v))
#print(v)
#print(v.real)
#print(v.imag)

#h=2*3
#print(type(h))

#h=2*3j   #j=1
#print(type(h))

#k=2j
#print(k.real)
#print(k.imag)

# 'Non primitive data type'
# List data type
# List: collection of elements stored in single variable
# we can update values
# we can add new items in list
# delete 
# list is a order
# indexing values
# different type of data can be stored
# declaration'

#g=list()
#g[]
#v=list()
#print('data type:',type(v))
#print(v)

'Day 6'
#operators
# arthmetic + - * / ** // %
#import time
#a=10
#b=23
#time.sleep(1.5)
#print(a+b)

#import time
#a='python'
#b='prg'
#time.sleep(1.5)
#print(a+" "+b)

#a='python'
#b=23
#print(a+b)

#a=10.25
#b=23.85
#print(a+b)

#r=3+7j
#y=6+8j
#print(r+y)

#a=True   #1
#b=False  #0
#print(a+b)

'list'
#a=[10,7,8]
#b=[6,8,4]
#print(a+b)

'tuple'
#a=(10,7,8)
#b=(6,8,4)
#print(a+b)

'Set'
# a={10,7,8}
# b={6,3,4}
# #print(a+b)
# res={*a,*b}
# print(res)


# a={'a':10,'b':7,'c':8}
# b={'a':6,'b':3,'c':4}
# #print(a+b)
# res={**a,**b}
# print(res)

'2-sep'
#while
# while True:
#     print('while loop')

# 'input'
# n=input("enter:")
# print(n)
# print(type(n))

# n=input('enter username:')
# while n!='soumya@25':
#     n=input('enter username:')
# print('username:',n)

# m=123
# temp=0                              
# while m!=0:                          #123!=0 
#     digit=m%10                       #digit= 123 % 10==>3      2               1
#     m//=10                           #12   1   0 
#     temp=temp*10+digit               #temp=temp*10+digit       3*10+2          32*10+1
# print(temp)                          #temp=0*10+3==>3          30+2==>32       320+1==>321


'fibonacci series'
# #0 1 1 2 3 4 5
# a,b=0,1                             #a=0 b=1       a=1   b=1           a=1    b=2        a=2   b=3
# for x in range(5):                  #        
#     print(a)                        #0            a=1                 a=1 
#     a,b=b,a+b                       #a=1  b=1     a=1    b=1+1=2      a=2    b=1+2=3

'perfect number'
# n=6     #1 2 3 4 5
# b=0
# for i in range(1,n):
#     if n%i==0:
#         b+=i            #sum of factors adds to b 
#         print("sum of factors:",b)
# if n==b:
#     print('perfect no')
# else:
#     print('not a perfect no')

'length finding'
# a=12345
# cou=0               #1     2          3        4         5
# while a!=0:             #12345!=0                       #1234!=0                  123!=0                        12!=0              1!=0        0=0
#     d=a%10               #d=5                           #d=4                      d=3                           d=2                d=1
#     a//=10               #1234                          #123                      12                            1                  0
#     cou+=1               #cou=cou+1=0+1==>1             cou=cou+1==1+1==>2        cou=cou+1==2+1==3             cou==3+1==4        4+1==5
#     print(cou)

# "prime numbers"
# n=5                                                          
# b=0
# for i in range(1,n+1):
#     if n%i==0:
#         b+=1
# #print(b)
# if b==2:
#     print("prime no",n)
# else:
#     print("not a prime no",n)


# n=5
# b=0
# for i in range(1,n):
#     if n%i==0:
#         b+=1
# #print(b)
# if b==1:
#     print("prime no",n)
# else:
#     print("not a prime no",n)


# 'even no and odd no'
# n=int(input('enter a no'))
# while True:
#     if n%2==0:
#         print("even no:",n)
#     else:
#         print("odd no",n)
#     break


# 'break'
# for x in range(1,10):
#     if x==5:
#         break
#     print(x)


# 'continue'
# for x in range(1,10):
#     if x==5:
#         continue
#     print(x)


# 'pass'
# for x in range(1,10):
#     if x==5:
#         pass
#     print(x)


'Day Sep-3'
# n=872354
# t=0
# while n!=0:
#     d=n%10
#     n//=10
#     cou=0
#     for x in range(1,d+1):
#         if d%x==0:
#             cou+=1
#     if cou==2:
#         t+=d
# print(t)

# 'Nested for loop or inner for loop'
# for x in range(1,6):
#     for y in range(1,11):
#         print(x,'X',y,'=',x*y)
#     print()


'Sep-15'

# res=[{'s_name':'pavithra','s_id':'101','s_mobile':'12345345'},
#      {'s_name':'sruthi','s_id':'102','s_mobile':'72345345'},
#      {'s_name':'soumya','s_id':'103','s_mobile':'612345345'},
#      {'s_name':'navya','s_id':'104','s_mobile':'412345345'},
#      {'s_name':'tina','s_id':'105','s_mobile':'412345345'},]
# # h=[]
# n=input('enter pin:')
# for x in res:
#     # res={}
#     if x['s_id']==n:
#         for a,b in x.items():
#             print(a,'=======',b)
#             # h.append(res)


'Sep-16'
# a={'a':10,'b':20}
# b={'c':50,'d':80}
# # res={**a,**b}
# # print(res)
# for key,value in b.items():
#     a[key]=value
# print(a)


# a=['a','b','c']
# b=[1,2,3]
# tem={}
# for x in range(len(a)):
#     print(a[x],'==',x,'===',b[x])
#     tem[a[x]]=b[x]
# print(tem)


# res={'a':10,'b':11,'c':12,'d':13}
# for x,y in res.items():
#     if y%2==0:
#         res[x]=y*2
# print(res)


# l=['karimnagar','warangal','jagtial']
# t={}
# for x in l:
#     t[x]=len(x)
# print(t)


'Sep -19'
'to print max value with max method'
# res={'a':100,'b':200,'c':300,'d':400}
# temp=max(sorted(res.items()))     #max, min, sum
# print(temp)

'to print max value without using max method'
# res={'a':100,'b':200,'c':300,'d':400}
# max=0
# e=''
# for x,y in res.items():
#     if y>max:
#         max=y
#         e=x
# print(e,"====",max)

'to convert keys to values and values to keys'
# res={'a':100,'b':200,'c':300,'d':400}
# tem={}
# for keys,values in res.items():
#     tem[values]=keys
# print(tem)

'to print count for certain key'
# res=[{'name':'soumya','dept':'cse'},
#      {'name':'pavithra','dept':'cse'},
#      {'name':'tina','dept':'it'},
#      {'name':'riya','dept':'eee'},]
# tem={}
# for x in res:
#     d=x['dept']
#     if d not in tem:
#         tem[d]=1
#     else:
#         tem[d]+=1
# print(tem)


'sorted orerder for both keys and values'
# res={'a':100,'b':800,'c':300,'d':400}
# tem=dict(sorted(res.items(),key = lambda item:item[1]))
# print(tem)

# res={'a':100,'h':800,'c':300,'d':400}
# tem=dict(sorted(res.items(),key = lambda item:item[0]))
# print(tem)


'Sep-22'
'List Compression'
# j='python developer'.split()
# r=[]
# for x in j:
#     r.append(len(x))
# print(r)

# r=[len(x) for x in j]
# print(r)


'table'
# s=[(2*x) for x in range(1,11)]
# print(s)


'factors of 10'
# n=10
# r=[]
# for x in range(1,n+1):
#     if n%x==0:
#         r+=[x]     # or  r.append(x)
# print(r)
        
# r=[x for x in range(1,n+1) if n%x==0]
# print(r)


'output=[[1],[2],[3]]'
# h=[]
# for x in range(1,4):
#     h+=[[x]]
# print(h)    

# h=[[x] for x in range(1,4)]
# print(h) 


'sum of no based on index'
# a=[10,20,30]
# b=[100,200,300]
# for x in range(len(a)):
#     print(a[x]+b[x])    
#     x+=1

# s=[(a[x]+b[x]) for x in range(len(a))]                      #s=[(x+y)for x,y in zip(a,b)]
# print(s)

'Flatten a 2D list into a 1D list using list comprehension.'
# mat=[[1,2,3],[6,5],[7,8,9]]
# r=[j for x in mat for j in x]
# print(r)

'Extract all digits from a given string. s = "abc123def456"'
# s = "abc123def456"
# r=[x for x in s if x.isdigit()]
# print(r)
    

'Create a list of all numbers from 1-100 that are divisible by both 3 and 5.'
# n=100
# s=[x for x in range(1,n+1) if x%3==0 and x%5==0]
# print(s)

'Build a list of tuples (number, square) for numbers from 1-10.'
# n=10
# s=[(x,x*x) for x in range(1,n+1) ]
# print(s)

'Print prime numbers between 10 to 50 using list comprehension'
# s=[x for x in range(10,50) if all(x%y!=0 for y in range(2,x))]
# print(s)
           
'Print order of character if is capital'
# s='SoUmYa'
# r=[ord(x) for x in s if x.isupper()]
# print(r)


'Sep-23'
# r=[10,11,13,12,14]
# s=['even' if x%2==0 else 'odd' for x in r]
# print(s)
# for x in r:
#     if x%2==0:
#         print('even')
#     else:
#         print('odd')


'[[1,2],[3,4],[5,6],[7,8],[9,10]] in one list'
# s=[[1,2],[3,4],[5,6],[7,8],[9,10]]
# r=[[x,x+1] for x in range(1,11,2) ]         
# r=[[x,x+1] for x in range(10) if x%2==1]
# print(r)

'print vowels from words'
# r=['python','java','c++']
# s=[y for x in r for y in x if y in 'AEIOUaeiou']
# print(s)
# for x in r:
#     for y in x:
#         if y in 'AEIOUaeiou':
#             print(y)
#         print()                  to get space


'r=[[1,2,3],[4,5,6],[7,8,9]]'      #[1,4,7],[2,5,8],[3,6,9]    t[0]
# for x in range(r(len(0))):
#     for x in r:
#       print(x)
'print prime or not'

# r=[[x,y] for x,y in enumerate(range(1,5))]
# print(r)

# r=['python','java','c++']  len(3) is print the word


'Write a list comprehension in Python that checks whether each number in a given list is "prime" or "not prime" and returns the result as a list.'
# n=[11,25,85,45]
# s=['prime' if all(x%y!=0 for y in range(2,x))  else 'not prime' for x in n]
# print(s)

'Using list comprehension, generate a 2D list with the following structure'
'input=[[1,2,3],[4,5,6],[7,8,9]] ==> output=[[1, 4, 7], [2, 5, 8], [3, 6, 9]]'
# r=[[1,2,3],[4,5,6],[7,8,9]]
# res=[[x[y]for x in r] for y in range(len(r[0]))]
# print(res)

'Using list comprehension, generate a list of tuples mapping ASCII values to characters for uppercase letters A, B, C.'
# r=['A','B','C','a']
# s=tuple((x,ord(x)) for x in r if x.isupper())
# print(s)

'tuple comprehsion'
'does not support python directly'
'(A,65),(B,66),(C,67),(D,68)'


'sep-29'
# s={x:x**2 for x in range(1,6)}
# print(s)

# s={x:x**2 for x in range(2,11,2)}
# print(s)

# w='success'
# s={x:w.count(x) for x in w }
# print(s)

# k=['a','b','c']
# v=[1,2,3]
# s={k[i]:v[i] for i in range(len(k))}
# print(s)

# d={'a':10,'b':20,'c':30}
# s={v:k for k, v in d.items()}
# print(s)

# s={x:x**2 for x in range(1,11) if x**2>10}
# print(s)

# l=['a','b','c']
# s={x.upper():ord(x.upper()) for x in l}
# print(s)

# s={x:('even' if x%2==0 else 'odd') for x in range(1,5)}
# print(s)

# words = ["apple", "banana", "kiwi"]
# s={word:len(word) for word in words}
# print(s)

# d = {'a': 5, 'b': 15, 'c': 25, 'd': 7}
# s={k:v for k,v in d.items() if v>10}
# print(s)

# s={x:{'square':x**2,'cube':x**3} for x in range(1,4)}
# print(s)

# asl={chr(x):x for x in range(97,123)}
# print(asl)

# words = ["cat", "dog", "bat"]
# s={word:word[::-1] for word in words}
# print(s)

# a=[0,1,2,3,4,5,6,7,8,9]
# s={'even': [x for x in a if x % 2 == 0],
#     'odd': [x for x in a if x % 2 != 0]}
# print(s)

# s={n: [i for i in range(1, n+1) if n % i == 0] for n in range(1, 6)}
# print(s)

# List=["hi", "hello", "world", "is", "great"]
# s={x:len(x) for x in List if len(x)>3}
# print(s)

# people = {'John': 15, 'Alice': 25, 'Bob': 19}
# s={k:v for k,v in people.items() if v>18}
# print(s)

# s={n:'prime' if all(n % i != 0 for i in range(2, n)) else 'notprime'
#     for n in range(2, 7)}
# print(s)

'oct 9'
# s='PYTHON'
# print(s[0:3])

# s='PYTHON'
# print(s[:4])

# s='PYTHON'
# print(s[2:])

# s='PYTHON'
# print(s[-4:-1])

# s='PYTHON'
# print(s[0:6:2])

# s='PYTHON'
# print(s[::-1])

# s='PYTHON'
# print(s[4:1:-1])

# s='PYTHON'
# print(s[-1:-5:-1])

# s='ABCDEFGHIJ'
# print(s[::2])

# s='SLICE'
# print(s[::])

# s='PYTHON'
# print(s[2:20])

# l=[10,20,30,40,50]
# print(l[1:4])

# l=[1,2,3,4,5,]
# print(l[::-1])

# l=[1,2,3,4,5,6]
# print(l[len(l)//2:])

# t=(1,2,3,4,5)
# print(t[3::-1])

# s='PYTHON'
# print(s[-3:])

# s='PYTHON'
# print(s[:-3])

# s='PYTHON'
# print(s[1:5:3])

# s='PYTHON'
# print(s[-1::-2])


'oct 10'
'check no is prime or not'



'between prime no '



'factorial, swap, factors'
# def swap(a,b):
#     a,b=b,a
#     print(a,b)
# swap(4,8)
'check even or odd'
# def check_even(a):
#     if a%2==0:
#         print('Even')
#     else:
#         print('Odd')
# check_even(8901)
# check_even(124)


# l='python'
# def length(l):
#     cou=0
#     for x in l:
#         cou+=1
#     print(cou)
# length(l)


# def max_value(lst):
#     max_num = None
#     for item in lst:
#         if isinstance(item, (int, float)):  
#             if max_num is None or item > max_num:
#                 max_num = item
#     return max_num
# data = [10, 'apple', 45, 'banana', 32]
# print("Maximum value:", max_value(data)) 


# def title_case(text):
#     words = text.split()
#     new_words = []
#     for word in words:
#         if len(word) > 0:
#             new_word = word[0].upper() + word[1:].lower()
#             new_words.append(new_word)
#     return ' '.join(new_words)
# sentence = "hello world this is python"
# print("Title case:", title_case(sentence))


'oct-13'
'int to str coversion'
# l=156
# tem=''
# s='0123456789'
# d=0
# while l>0:
#     d=l%10
#     l//=10  
#     for x in range(len(s)):
#         if d==x:
#             tem=s[x]+tem
# print(tem,'==',type(tem))


'swap'
k='python'
# def swap_case(a):
#     res=''
#     for x in k:
#         if ord(x)>=65 and ord(x)<=90:
#             d=ord(x)+32
#             res+=chr(d)
#         elif ord(x)>=97 and ord(x)<=122:
#             d1=ord(x)-32
#             res+=chr(d1)
#     print(res)
# swap_case('PyTHon')


# def even(n):
#     if n%2==0:
#         return 'even'
#     else:
#         return 'odd'
# print(even(5))


# def even(a,b):
#     env=[]
#     for x in range(a,b):    
#         if x%2==0:
#             env+=[x]
#     return env             #if we use return key word must use print  
# even(10,20)
# print(even(10,20))


# def title(t):
#     return t.title()
# print(title('hello world'))


# def feb(a,b):
#     for x in range(0,5):
#         print(a)
#         a,b=b,a+b
# feb(0,1)


# def palin(a,b):
#     p=a,b
#     tem=0
#     for x in range(a,b):
#         d=x%10
#         x//=10
#         tem=tem*10+d
#     if p==tem:
#         print("palindrome")
#     else:
#         print("not palindrome")
# palin(20,40)


# def armstrong(start,end):
#     for num in range(start,end+1):
#         digits=str(num)
#         power=len(digits)
#         total=sum(int(d)**power for d in digits)
#         if total==num:
#             print(num,end=" ")
# armstrong(1,1000)


# def gcd(a,b):
#     while b!=0:
#         a,b=b,a%b
#     return a
# print(gcd(10,20))


# def cal():
#     while True:
#         n1=int(input('enter 1st no'))
#         n2=int(input('enter 2nd no'))
#         s=input('enter any symbol')
#         if s=='+':
#             print(n1+n2)
#         elif s=='-':
#             print(n1-n2)
#         elif s=='*':
#             print(n1*n2)
#         elif s=='/':
#             if n1==0 or n2 ==0:
#                 print("error")
#             else:
#                 print(n1/n2)
#         elif s=='%':
#             print(n1%n2)
#         user=input("")
#         if user=='exit':
#             break
# cal()

'oct-15'
'oct-16'
'oct-17'
# import random
# for x in range(5):
#     print(random.randint(6000000000,9999999999))

help("modules")