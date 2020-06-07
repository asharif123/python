##A class is like a blueprint that ensures the consistent creation of instances.
#Ex: x = 5 means that the variable x is an instance of the integer value!
#Attributes: Characteristics shared by all instances of the class type.
#Ex: name, account balance and email are characteristics of a banking app
#Methods: Actions that an object can perform. A user, for example, should be able to make a deposit or a withdrawal, or maybe send money to another user.
# Attributes are defined in a "magic method" called __init__
class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount

##initiate users
guido = User("Guido von Rossum", "guido@python.com")
monty = User("Monty Python","monty@python.com")

print(guido.name,guido.email)
print(monty.name,monty.email)

guido.make_deposit(5000)
monty.make_deposit(3000)

print(guido.account_balance)
print(monty.account_balance)
