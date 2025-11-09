from abc import ABC,abstractmethod
import random
class Bank():
    @abstractmethod
    def create_acc(self):
        pass
    def deposit(self):
        pass
    def withdraw_amount(self):
        pass
    def details(self):
        pass
class union(Bank):
    
    def create_acc(self):
        self.name=input('enter name')
        self.mobile=int(input('enter mobile no'))
        self.account_no=random.randint(00000000000,99999999999)
        self.balance=500
        print('Account no:',self.account_no)
        print('Account created successfully')
    
    def deposit(self):
        self.acc_no=int(input('enter account no:'))
        self.deposit_a=int(input('enter ammount:'))
        if self.acc_no==self.account_no:
            self.balance+=self.deposit_a
        else:
            print('invalid account no')
        print('deposit process')
        print('your balance',self.balance)
    
    def withdraw_amount(self):
        self.Acc_no=int(input('enter account no:'))
        self.withdraw_a=int(input('enter ammount:'))
        if self.Acc_no==self.account_no and self.balance>self.withdraw_a:
            self.balance-=self.withdraw_a
        else:
            print('check balance')
        print('withdraw process')
        print('your balance',self.balance)
    
    def details(self):
        print('Details')
        print('Name:',self.name)
        print('mobile:',self.mobile)
        print('account no:',self.account_no)
        print('balance:',self.balance)

obj=union()
while True:
    print(""" enter 1 create account
          enter 2 deposit
          enter 3 withdraw ammount
          enter 4 details
          enter 5 exit""")
    n=int(input('enter a num'))
    if n==1:
        obj.create_acc()
    elif n==2:
        obj.deposit()
    elif n==3:
        obj.withdraw_amount()
    elif n==4:
        obj.details()
    elif n==5:
        break


from abc import ABC,abstractmethod
class vehicle():
    @abstractmethod
    def start_engine(self):
        pass
    def stop_engine(self):
        pass
    def fuel_status(self):
        print('fuel level is good')
class Car(vehicle):
    def start_engine(self):
        print('car engine is started')
    def stop_engine(self):
        print('car engine is stoped')
class Bike(vehicle):
    def start_engine(self):
        print('bike engine is started')
    def stop_engine(self):
        print('bike engine is stopped')
car=Car()
bike=Bike()

car.start_engine()
car.stop_engine()
car.fuel_status()

bike.start_engine()
bike.fuel_status()
bike.stop_engine()