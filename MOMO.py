#This system works by entering your security pin first
print('Welcome to Qtigo Money')
restart=('Y')
chances = 3
balance = 67.14
while chances >= 0:
    pin = int(input('Please Enter Pin: '))
    if pin == (1234):
        print('Access granted!\n')
        while restart not in ('n','NO','no','N'):
            print('Please Press 1 For Your Balance\n')
            print('Please Press 2 To Make a Withdrawal\n')
            print('Please Press 3 to Buy Aitime \n')
            print('Please Press 4 To Exit \n')
            option = int(input('Choose to proceed: '))
            if option == 1:
                print('Your Balance is GH₵',balance,'\n')
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawal = float(input('How Much Would you like to withdraw? \‎GH₵10/‎GH₵20/‎GH₵40/‎GH₵60/‎GH₵80/‎GH₵‎100 for other enter 1: '))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawal
                    print ('\nYour Balance is now ‎GH₵,balance')
                    restart = input('Would You you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawal != [10, 20, 40, 60, 80, 100]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawal == 1:
                    withdrawal = float(input('Please Enter Desired amount:'))    

            elif option == 3:
                Amount= float(input('Enter Amount? '))
                balance = balance + Amount
                print ('\nYour Balance is now GH₵',balance)
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Thank you for you service')
                break
            else:
                print('Please Enter a correct pin\n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Pin')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries, Accout suspended')
            break
