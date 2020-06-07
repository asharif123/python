#used for visualizations!
import pygal
from random import randint
class Die():
##
##    def __init__(self):
##        self.rolls = []
    def roll_die(self):
        number = randint(1,6)
        return (number)

##game = Die()
##game.roll_die()


#print first 100 rolls and store in the results list using 'Die' class!!
game = Die()
results = []
num = 0
while num < 100:
    value = game.roll_die()
    results.append(value)
    num = num + 1
print (results)

#print the number of times 1 to 6 appears in results!
frequencies = []
for value in range(1,7,1):
#.count(value) counts the number of times 'value' appears in 'results'
    frequency = results.count(value)
    frequencies.append(frequency)

#Create a bar graph using the instance .Bar()
graph = pygal.Bar()
graph.title('Graph of number of times 1 to 7 appears in results!')
graph.x_labels['1','2','3','4','5','6']
graph.y_labels[frequencies]
#add a series of labels to the chart!!
graph.add('D6',frequencies)
