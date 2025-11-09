'swap'
k='python'
def swap_case(a):
    res=''
    for x in k:
        if ord(x)>=65 and ord(x)<=90:
            d=ord(x)+32
            res+=chr(d)
        elif ord(x)>=97 and ord(x)<=122:
            d1=ord(x)-32
            res+=chr(d1)
    print(res)
swap_case('PyTHon')


def factors():
    n=10
    r=[]
    for x in range(1,n+1):
        if n%x==0:
            r+=[x]     
    print(r)

def prime():
    n=5                                                          
    b=0
    for i in range(1,n+1):
        if n%i==0:
            b+=1
#print(b)
    if b==2:
        print("prime no",n)
    else:
        print("not a prime no",n) 