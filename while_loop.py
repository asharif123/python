##count = 0
###prints from 1 thru 9, while count is less than 10, print count
###0,1,2,3,4,5,6,7,8,9
##while count < 10:
##  print ("Hello, I am a while loop and count is = ", str(count))
##  count = count + 1

  



###print the square of numbers 1 thru 10 
##num = 1
##
##while num < 11: 
##  # Fill in the condition
##  # Print num squared
##  # Increment num (make sure to do this!)
##  print (num ** 2)
##  num = num + 1
#1,4,9,16,25,36,49,64,81,100
####as long as choice input does NOT equal to y or n, keep printing "Sorry I didn't catch that"
##choice = raw_input('Enjoying the course? (y/n)')
##
##while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
##  choice = raw_input("Sorry, I didn't catch that. Enter again: ")

##0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19
count = 0

while count < 20:
  print (count)
  count = count + 1
  if (count == 12):
    continue


import random

##print "Lucky Numbers! 3 numbers will be generated."
##print "If one of them is a '5', you lose!"
##
##
##
##
##chances = 0
##while chances < 3:
##  for x in range(3):
##    num = random.randint(1, 6)
##    print num
##    chances = chances + 1
##  if (chances == 3):
##    print ("Game over!")
##    break
##    if num == 5:
##      print "Sorry, you lose!"
##      break
##    else:
##      print "You win!"
##      break



##import random
##
##### Generates a number from 1 through 10 in 3 guesses using while loop
####print "You have 3 chances to select a number from 1 to 10!"
####print "IF you fail to guess the correct number 3 times, you lose!"
##guess = 3
##number = random.randint(1,30)
##while guess > 0:
##  value = int(raw_input("Choose a number from 1 to 30: "))
##  if (value == number):
##    print "You have guessed the correct number!"
##    break
##  else:
##    print "Try again! \n"
##    guess = guess - 1
##    if guess == 0:
##      print ("Sorry, the correct number is %s") %(number)
##      break
  
    


phrase = "A bird in the hand..."

##comma after statement ensures everything printed is on the same line!!
#Ex: characters in phrase are printed on same line as "A bird in the hand..."
##and not in downward fashion!!!
##for char in phrase:
##  if (char == "A") or (char == "a"):
##  	print "X",
##  else:
##    print char,

#####Iterate thru dictionary
##d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
##
##for key in d:
##  # print the key of each pair, ex: 'a', 'b', 'c'
##  print key
##  #print the pair of each key, ex: 'apple'
##  print d[key]

####choices = ['pizza', 'pasta', 'salad', 'nachos']
####
####print 'Your choices are:'
####for index, item in enumerate(choices):
####  print index + 1,
####
####
#####zip creates pairs of elements from 2 or more lists and stops at end of shorter
#####list!
#####iterate over multiple lists, prints out the end of shorter lists!
#####Ex: stop printing at 5th entry of list_a
####list_a = [3, 9, 17, 15, 19]
####list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
####
####for a, b in zip(list_a, list_b):
####  # Add your code here!
####  print a
####
####
####Iterate thru fruits, if tomato in fruit, print "A tomato is not a fruit!"
####Initially prints "A tomato is not a fruit" and then prints tomato
####Without break in for/else, for loop ends normally and stuff under else is executed
##fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
##
##print 'You have...'
##for f in fruits:
##  if f == 'tomato':
##    print 'A tomato is not a fruit!'
##     # (It actually is.)
##    break  
##  print 'A', f
##else:
##  print 'A fine selection of fruits!'

