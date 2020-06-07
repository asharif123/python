##If no arguments are provided, the function should return a random integer between 0 and 100.
##If only a max number is provided, the function should return a random integer between 0 and the max number.
##If only a min number is provided, the function should return a random integer between the min number and 100
##If both a min and max number are provided, the function should return a random integer between those 2 values.

import random
def randInt(min=0, max=100):
    num = random.random()*max
    if (min > 0) and (max == 100):
        return round((random.random()*(100-min))+min)
    if (min > 0) and (max != 100):
        value = (random.random()*(max-min))+min
        return round(value)
    else:
        return round(num)

while True:
    print(randInt(min=50,max=500))


