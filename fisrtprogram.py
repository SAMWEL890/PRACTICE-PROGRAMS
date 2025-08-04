class Account:
    def __init__(self, acc_no, bal):
        self.balance = bal
        self.account_no = acc_no
    dict = {
         1 : "Debit",
         2 : "Credit",
         3 : "Get Balance",
         4 : "Exit"
    }

    def holder(self,acc_holder):
            self.account_holder = acc_holder

    def debit(self,amount):
        self.balance -= amount
        print(f"Debited amount: {amount}")
        print(f"Total remaining balance in account {self.account_no} is {self.get_balance()}")
    
    def credit(self,amount):
        self.balance += amount
        print(f"Credited amount: {amount}")
        print(f"Total remaining balance in account {self.account_no} is {self.get_balance()}")

    def get_balance(self):
        return self.balance

acc1 = Account(input("Enter account number:" ),int(input("Enter balance:" )))
acc1.holder(input("please provide the name of account holder: "))
while True:
    print(f"Welcome to the banking system {acc1.account_holder}")
    for key, value in acc1.dict.items():
        print(f"{key}. {value}")
    i = int(input("Please select a value given above: "))
    if i == 1:
        acc1.debit(int(input("Enter your debiting amount: ")))
    elif i == 2:
        acc1.credit(int(input("Enter your crediting amount: ")))
    elif i == 3:
        print(f"Your current balance is {acc1.get_balance()}")
    elif i == 4:
        print("Thank you for using our banking system.")
        break
    else:
        print("Invalid option selected.")
