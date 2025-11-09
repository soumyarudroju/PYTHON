num=-85
if num>0:
    print("positive number")
elif num<0:
    print("negative num")
else:
    print("zero")

num=85
if num%2==0:
    print("even no")
else:
    print("odd no")

num1=78
num2=89
if num1>num2:
    print("num1 is larger")
else:
    print("num2 is is larger")

num1=56
num2=58
num3=24
if num1>num2 & num1>num3:
    print("num1 is greater")
elif num2>num1 & num2>num3:
    print("num2 is greater")
else:
    print("num3 is greater")

age=25
if age>=18:
    print("the candiadte is eligible for vote")
else:
    print("the candidate is not eligible for vote")

marks=85
if marks>=95:
    print("student got A")
elif marks>=75:
    print("student got B")
elif marks>=50:
    print("student got C")
else:
    print("student is Failed")

vovel=('A','E','I','O','U','a','e','i','o','u')
char='a'
if char in vovel:
    print("It is a Vovel")
else:
    print("It is a Consonent")

num=15
if (num%3==0&num%5==0):
    print("num is multiple by 3 and 5")
else:
    print("num is not multiple by 3 and 5")

char='8' 
if char.isupper():
    print("it is upper case")
elif char.islower():
    print("it is lower case")
elif char.isdigit():
    print("it is a digit")
else:
    print("it is a special symbol")

num=45
if num%7==0:
    print("num is divisible by 7")
else:
    print("num is not divisible by 7")

age=57
if age>=60:
    print("the person is a senior citizen")
else:
    print("the person is not a senior citizen")