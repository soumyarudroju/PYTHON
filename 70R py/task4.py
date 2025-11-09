amount=5800
if amount>5000:
   a=amount*20/100
   print("discount amount is",a)
elif 2000<=amount<=5000:
   b=amount*10/100
   print("discount amount is",b)
else:
   print("discount is not applied")

pin1=2025
pin2=2140
if pin1==pin2:
   print("Access Granted")
else:
   print("Access Denied")


num=568
years=num//365
remnum=num%365
months=remnum//30
smallrem=remnum%30
print("year:",years,"months:",months,"smallrem",smallrem)

amount=156312
note500=amount//500
remnote500=amount%500

note200=remnote500//200
remnote200=remnote500%200

note100=remnote200//100
remnote100=remnote200%100

note50=remnote100//50
remnote50=remnote100%50

note20=remnote50//20
remnote20=remnote50%20

note10=remnote20//10
remnote10=remnote20%10

note5=remnote10//5
remnote5=remnote10%5

note2=remnote5//2
remnote2=remnote5%2

note1=remnote2//1
remnote1=remnote2%1
print("note500",note500 ,"note200", note200,"note100",note100 ,"note50",note50 ,"note20",note20 ,"note10",note10 ,"note5",note5 ,"note2",note2 ,"note1",note1)