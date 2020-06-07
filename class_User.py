##create a Bank class
class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def make_deposit(self,deposit):
        self.balance += deposit
       

    def make_withdrawal(self,amount):
        if amount < self.balance:
            self.balance -= amount

    def display_bank_balance(self):
        print("Total balance in " + self.name + "'s" + " account = " + "$" + str(self.balance))

#have the first user transfer money to the third user and then print both users' balances
    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print("\n$" + str(amount) + " has been transferred from " + self.name + "'s account to " + (other_user.name) + "'s account.")
        
awad = Bank("Awad",33000)
for i in range(3):
    awad.make_deposit(5000)
awad.make_withdrawal(5000)
awad.display_bank_balance()

jimmy = Bank("Jimmy",41000)
for i in range(2):
    jimmy.make_deposit(12000)
for i in range(2):
    jimmy.make_withdrawal(1000)
jimmy.display_bank_balance()



jackson = Bank("Jackson",55000)
jackson.make_deposit(4000)
for i in range(3):
    jackson.make_withdrawal(7000)
jackson.display_bank_balance()

awad.transfer_money(jackson,1200)
awad.display_bank_balance()
jackson.display_bank_balance()

        
