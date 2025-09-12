amount=1000

input2=str(input('enter input query'))

if(input2=="withdrawal"):
    Withdrawal_amount =int(input("enter amount you want to withdraw"))
    if(Withdrawal_amount>amount):
        print("insufficient balance")
    else:
        print("remaining balance: ",amount-Withdrawal_amount)
      
elif(input2=="deposit"):
    Deposit_amount =int(input("enter amount you want to deposit"))
    amount=amount+Deposit_amount
    print("remaining balance: ",amount)
    
elif(input2=="check balance"):
    print(amount)
else:
    print("invalid input")