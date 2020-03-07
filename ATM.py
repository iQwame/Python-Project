print('Welcome to the ATM by Q')
print('Enter account number and pin to continue')

count=0
while count < 3:

    Pin = input('Enter Pin: ')
    if Pin =='0627':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1


class Bank_Account: 

    def __init__(self): 

        self.balance=0

        print("Welcome to the ATM by Q")
    

    def deposit(self): 

        amount=float(input("Enter amount to be Deposited: ")) 

        self.balance += amount 

        print("\n Amount Deposited:",amount) 

    def withdraw(self): 

        amount = float(input("Enter amount to be Withdrawn: ")) 

        if self.balance>=amount: 

            self.balance-=amount 

            print("\n You Withdrew:", amount) 

        else: 

            print("\n Insufficient balance  ") 

    def display(self): 

        print("\n Net Available Balance = ",self.balance) 

   
# creating an object of class 

s = Bank_Account() 

   
# Calling functions with that class object 
s.deposit() 
s.withdraw() 
s.display()

