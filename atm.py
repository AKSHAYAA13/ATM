import re
def check_number(name):
    pattern = r'\d'
    return bool(re.search(pattern, name))
def user_name():
    text = input("Enter the account holder name: \n")
    return text
def check_space(name):
    return ' ' in name
def check_loop():
    while True:
        name = user_name()
        if check_space(name):
            name = name.replace(" ", "")
            while check_number(name):
                print("Name should not contain numbers. Kindly enter again.")
                name = user_name()
            break
        else:
            while check_number(name):
                print("Name should not contain numbers. Kindly enter again.")
                name = user_name()
            break
    return name
class account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        print("\nAccount holder name:",owner)
        print("Account balance:",balance,"\n")
    def deposit(self,amount=0):
        self.amount=amount
        self.balance=amount+self.balance
        return(self.balance)
    def withdraw(self,draw=0):
        self.draw=draw
        bal=self.balance
        if self.balance>=2000:
            bal=bal-draw
            if bal<1000:
                return(0)
            else:
                self.balance=self.balance-draw
                return(self.balance)
        elif bal>1000:
            bal=bal-draw
            if bal<1000:
                return(0)
            else:
                self.balance=self.balance-draw
                return(self.balance)
        elif self.balance==1000:
            return(1)
txt="Welcome to our bank!!\n"
print(txt.center(150))
a=check_loop()
b=eval(input("Enter the minimum amount 1000\n"))
while b<1000:
    b=eval(input("Enter the initial amount 1000\n"))
acc1=account(a,b)
while True:
    print("\nselect the number to proceed further")
    ans=eval(input('''Enter the respective number
    \t* Balance checking - Enter number 1
    \t* Deposit - Enter number 2
    \t* Withdraw - Enter number 3
    \t* Exit or Logout - Enter number 4\n'''))
    if ans==1:
        print("\nThe Available balance is",acc1.balance)
    elif ans==2:
        d=eval(input("\nEnter the amount to be deposit\n"))
        while d<500:
            print("\nThe maximum amount to deposit 500\n")
            d=eval(input("\nEnter the amount to be deposit\n"))
        acc1.deposit(d)
        print(d,"Rupees has been deposited successfully\n")
    elif ans==3:
        w=eval(input("\nEnter the amount to be withdraw\n"))
        while w<500:
            print("\nThe maximum amount to withdraw 500\n")
            w=eval(input("Enter the amount to be withdraw\n"))
        while w>acc1.balance:
            print("\ncheck the balance and enter the withdraw amount\n")
            w=eval(input("\nEnter the amount to be withdraw\n"))
        wr=acc1.withdraw(w)
        if wr==1:
            print("\nTheir no sufficient amount to withdraw\n")
        elif wr==0:
            print("\nYou cant withdraw, the amount you entered because it will affect the minimum balance\n")
        else:
            print(w,"Rupees has been withdraw successfully\n")
    elif ans==4:
        break
    else:
        print("\nEnter the mentioned number for smooth process\n")
print("You have successfully logout from the current transaction\n")
