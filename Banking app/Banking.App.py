menu = '''---------------------- 
Banking System 1.0\n---------------------- 
1. Check Available Balance 
2. Withdraw Cash 
3. Deposit Cash 
4. Transfer Money 
0. Exit\n---------------------- 
''' 
  
amount = 0.0 
while True: 
    print(menu) 
    option = int(input('Select Option from Menu: ')) 
    if option == 0: 
        print("Terminating Program......") 
        break 
    elif option == 1: 
        print(f"Your current balance is: {amount}") 
    elif option == 2: 
        
        #ask user to enter amount they wish to withdraw 
        # store the amount in a variable called "withdrawal_amount"
        #convert it to a float
        withdrawal_amount = float(input("Enter amount to withdraw: ")) 
        #check if it is possible to withdraw that amount
        if withdrawal_amount <= amount: 
            final_amount = amount - withdrawal_amount
            print(f"Initial balance was: {amount}")
            print(f"Final Blance after withdrawing {withdrawal_amount} is: {final_amount}")
            amount = final_amount
        else: 
            amount = amount - 0
            print(f"You have insufficient funds. Your current balance is only: {amount}")
    elif option == 3: 
        cash = float(input("deposit amount: ")) 
        print(f"Initial Balance was: {amount}") 
        amount += cash 
        print(f"Final Balance after depositing {cash} is: {amount}") 
    elif option == 4: 
        #create a new variable " recipient_name"
        #user enter the recipient name and it is stored in that variable. 
        recipient_name = input("Enter recipient name:")
        # create a new variable transfer_amount and convert it to a float.
        #user enters the amount and stored in that variable.  
        transfer_amount = float(input("Enter amount to transfer:"))
        # check whether it is possible to transfer entered amount
        if transfer_amount <= amount:
            famount = amount - transfer_amount
            print(f"initial balance was: {amount}")
            print(f"Transfer of {transfer_amount} to {recipient_name} successful.")
            print(f"Final Balance is: {famount}")
            amount = famount
        else:
            amount = amount - 0
            print(f"Insufficient funds. Cannot transfer {transfer_amount}. Current balance is: {amount}")
        
        
    else: 
        print("Option not available") 
  
print("Have a nice day!")