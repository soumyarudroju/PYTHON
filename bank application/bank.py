import random
class Bank:
    Holder_Details=[]
    def create_new_Account(self):
        print('**==** Welcome to Union Bank **==**')
        new_Holder={}
        new_Holder['Holder_Name']=input('Enter Holder name:')
        new_Holder['Aadhar_Number']=input('Enter Aadhar number:')
        new_Holder['Mobile']=input('Enter Holder Mobile number:')
        new_Holder['IFSCCODE']='IFSC05235'
        new_Holder['Account_Number']=random.randint(1111111111,9999999999)

        Type_of_Account=input('Select Account Type Saving/Zero:').lower()
        while True:
            if Type_of_Account=='saving':
                print('Your Account is Saving, You have to deposit 500 rupees.')
                s_Account=int(input('Deposit 500 rupees:'))
                if s_Account==500:
                    new_Holder['Sufficient_Balance']=s_Account
                    break
                else:
                    print('== Please Deposit 500 rupees then only your Account Created! ==')
            if Type_of_Account=='zero':
                print('Your Account is Zero, You have to deposit 100 rupees.')
                s_Account=int(input('Deposit 100 rupees:'))
                if s_Account==100:
                    new_Holder['Sufficient_Balance']=s_Account
                    break
                else:
                    print('== Please Deposit 100 rupees then only your Account Created! ==')
        Bank.Holder_Details.append(new_Holder)
        print(Bank.Holder_Details)
    
    def Deposit(self):
        print('== Welcome to Deposit option ==')
        n1=input('Enter Holder name:')
        n2=int(input('Enter Account number:'))
        n3=int(input('Enter Deposit money:'))
        for x in Bank.Holder_Details:
            if x['Holder_Name']==n1 and x['Account_Number']==n2:
                x['Sufficient_Balance'] += n3
                print("Deposit successful!")
                break
            else:
                print("No account found with given details.")
        print(Bank.Holder_Details)

    def with_draw(self):
        print('== Welcome to Withdraw option ==')
        p1=input('Enter Holder name:')
        p2=int(input('Enter Account number:'))
        p3=int(input('Enter Withdraw money:'))
        for x in Bank.Holder_Details:
            if x['Holder_Name']==p1 and x['Account_Number']==p2:
                if x['Sufficient_Balance']>=p3:
                    x['Sufficient_Balance']-=p3
                    print(f"Withdraw Successful. Remaining Balance:{x['Sufficient_Balance']}")
                    break
                else:
                    print('Insufficient balance. Please check your balance once.')
            else:
                print('Account not found.')
            print(Bank.Holder_Details)

    def Details(self):
        t1=input('Enter Holder name:')
        t2=int(input('Enter Account number:'))
        for x in Bank.Holder_Details:
            if x['Holder_Name']==t1 and x['Account_Number']==t2:
                for a,b in x.items():
                    print(a,'==>',b)
    
    def Check_Balance(self):
        t10=input('Enter Holder name:')
        t20=int(input('Enter Account number:'))
        for x in Bank.Holder_Details:
            if x['Holder_Name']==t10 and x['Account_Number']==t20:
                print('Balance==>:',{x['Sufficient_Balance']})
                return

obj=Bank()
while True:
    print('''\n--- Bank Menu ---
1)Create New Account
2) Deposit
3) Withdraw
4) Account Details
5) Check Balance
6) Exit ''')
    choice=input('Choose an optin (1-6):')
    if choice=='1':
        obj.create_new_Account()
    elif choice=='2':
        obj.Deposit()
    elif choice=='3':
        obj.with_draw()
    elif choice=='4':
        obj.Details()
    elif choice=='5':
        obj.Check_Balance()
    elif choice=='6':
        print('Thank you for using the banking system.')
        break
    else:
        print("Invalid option. Please choose between 1 to 6.")