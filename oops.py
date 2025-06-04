class Account:
    
    accNumber = 0
    def __init__(self,accnum):
        self.accNumber = accnum
        self.balance = 5000 
    def printBalance(self):
        print("Your Account Number is: "+str(self.accNumber))
        print("And your balance is: "+str(self.balance))
    def credit(self,amt):
        self.balance += amt
        self.printBalance()
    def debit(self,amt):
        if(self.balance>=amt):
            self.balance-=amt
            self.printBalance()
        else:
            print("Insufficent Balance...")

num = input("Enter your Account Number: ")
aa = Account(num)
choice = int(input("Enter 1 for credit and 0 for debit: "))
if(choice==0):
    amt = int(input("Enter the amount you want to debit: "))
    aa.debit(amt)

elif(choice==1):
    amt = int(input("Enter the amount to be credited: "))
    aa.credit(amt)
