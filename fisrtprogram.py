class Account:
    def __init__(self, acc_no, bal):
        self.balance = bal
        self.account_no = acc_no
    
    def holder(self,acc_holder):
            self.account_holder = acc_holder
            print(f"Account number:{self.account_no} is belong to {self.account_holder}")

    def debit(self,amount):
        self.balance -= amount
        print(f"Debited amount{amount}")
        print(f"Remaining balance is {self.balance}")
    
    def credit(self,amount):
        self.balance += amount
        print(f"Credited amount {amount}")
        print(f"Remaining balance is {self.balance}")
    
    def get_balance(self):
        return self.balance

acc1 = Account(input("Enter account number:" ),input("Enter balance:" ))
acc1.holder(input("please provide the name of account holder: "))
acc1.debit(int(input("enter your amount" )))
acc1.credit(50000)
print(f"Total remaining balance in account {acc1.account_no} is {acc1.get_balance()}")
print(f"THANKS FOR JOINING US")

acc2 = Account(20000000, 707045)
acc2.holder(input("please provide the name of account holder: "))
acc2.debit(int(input("enter your amount" )))
acc2.debit(60000)
acc2.credit(100000)
print(f"Total remaining balance in account {acc2.account_no} is {acc2.get_balance()}")
print(f"THANKS FOR JOINING US")