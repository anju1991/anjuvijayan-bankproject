#Account login
name=input("Please enter your username :")
dob=input("Date of birth :")
password=name+dob
print("password :",password[0]+"*"*(len(password)-1)+password[-1])

if  password ==name+dob:
    print("Login successfull")
else:
    print("Login failed.Please try again.")
#Create Account
def create_account():
    print("Welcome to the bank")
    name= input("Please enter your name :")
    balance=0
    account ={"name":name,"balance":balance}
    print("Account created successfully.")
    return account


#Deposit
def deposit(account,amount):
    account["balance"]+=amount
    print("deposit is successful.")
#Withdraw
def withdraw(account,amount):
    if amount>account["balance"]:
        print("Insufficient funds.")
    else:
        account["balance"]-=amount
        print("Withdrawal successfull.")
#Check Balance
def check_balance(account):
    print("your current balance is :",account["balance"])

account = create_account()

while True:
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Checkbalance")
    print("4.Exit")
    option=int(input("Enter your option :"))
    if option==1:
        amount=int(input("Enter the amount to deposit:"))
        deposit(account,amount)
    elif option==2:
        amount=int(input("Enter the amount to withdraw :"))
        withdraw(account,amount)
    elif option==3:
        check_balance(account)
    elif option==4:
        print("Thank you for using the bank")
        break
    else:
        print("invalid option.Try again.")

