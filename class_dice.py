#import pygal
from random import randint
class Die():

    def __init__(self,number_rolls):
#User enters the number of times he wants to roll a dice!
        self.number_rolls = number_rolls
    def roll_die(self):
        num = 0
        number = randint(1,6)
        return (number)

##game = Die(1000)
##rolls = []
##num = 0
###print (game.number_rolls)
##while num < game.number_rolls:
##    rolls.append(game.roll_die())
##    num = num + 1
##print (rolls)
##
####print number of that that the numbers 1 to 7 are rolled using .count()
##results = []
##for value in range(1,7,1):
##    total = rolls.count(value)
##    results.append(total)
##print (results)
