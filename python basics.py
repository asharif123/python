##print "Hello world!"
##message = "Hello world I am learning something!"
##print message
##
###List comprehension!
##cubes = [x**3 for x in range(1,11,1)]
##print cubes
##
##message = "Hello world I am learning something!"
###Using .title() capitalizes first letter of each word that comes after whitespace!
##print message.title()
##print "Asdfsdfadsgsgadsfasdfdsaf".title()
###Capitalizes all letters ih message
##print message.upper()
###lower cases all letters
##print message.lower()

#####Calculate restaurant bill!###
##meal = 44.50
##tip = 0.15
##tax = 0.0675
## 
##total = meal + (meal * tax)
##bill = total + (total * tip)
##
##print(bill)
##
#######Use backslash to separate apostrophe from string#####
##'This isn\'t flying!'
##
####Print fifth letter from string "MONTY"
##fifth_letter = "MONTY"[4]
##print fifth_letter
##
###print length of string!
##
##sentence = "Welcome to python!"
##print(len(sentence))
##
######Use str to Turns anything into strings
##pi = 3.14
##str(pi)
##print(pi)
##
###Turn 3.14 into a string on line 3! Use space between 3.14 and around
##
##print "The value of pi is around " + str(3.14)
##
####String formatting example
##string_1 = "Camelot"
##string_2 = "place"
##
##print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)
##
##Raw_input string format examples
name = str(input("What is your name? "))
age = int(input("How old are you? "))
color = str(input("What is your favorite color? "))

print ("So you go by the name %s, you are %s years old, and your favorite color is %s.") %(name, age, color)

