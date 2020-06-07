class BankAccount:
    def __init__(self,balance=0,interest_rate=0,name=''):
        self.balance = balance
        self.interest_rate = interest_rate
        self.name = name

    def display_account_info(self):
        print("Account name:", self.name)
        print("Balance: $", self.balance)
        return self

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
#store all the accounts that are made by one user
        self.accounts = []
#balance,interest,and name are inputted by the user
    def create_bank_account(self,balance,interest_rate,name):
        account = BankAccount(balance,interest_rate,name)
        self.accounts.append(account)

    def display_bank_balance(self):
        for account in self.accounts:
            account.display_account_info()

##SENSEI BONUS
awad = User('awad','awadsharif9@gmail.com')
awad.create_bank_account(1000,0.02,"checking")
awad.create_bank_account(2000,0.01,"saving")
awad.create_bank_account(3000,0.01,"banking")

awad.display_bank_balance()
