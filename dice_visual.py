#import pygal
from random import randint
class Die():

    def __init__(self,sides):
#User enters the number of sides on each dice!
        self.sides = sides
#ROLLS A NUMBER FROM 1 TO 6!
    def roll_die(self):
        num = 0
        number = randint(1,self.sides)
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
