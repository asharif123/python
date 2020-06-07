integers = [1,2,3,4,5,6,7,8,9]
for integer in integers:
    if integer == 1:
        print (str(1) + 'st' + '\n')
    elif integer == 2:
        print (str(integer) + 'nd' + '\n)
    elif integer == 3:
        print (str(3) + 'rd' + '\n')
    else:
        print (str(integer) + 'th' + '\n')



###print only even numbers, use continue to skip odd numbers!
##for value in range(1,11):
##    if (value % 2 != 0):
##        continue
##    print value
##
##for i in range(1,6):
##    print i
##while True:
##    number = int(raw_input("Please enter an integer: "))
##    if (number % 10) == 0:
##        print ("%s is a multiple of 10!" + "\n") %(number)
##    else:
##        print ("%s is not a multiple of 10!" + "\n") %(number)
##        break

###Type in X to break out of infinite loop!
##while True:
##    entry = str(raw_input("Type in X to exit: ")).upper()
##    if entry == "X":
##        print "Exiting the program!"
##        break

##current_users = ['JOHN', 'asharif', 'Jimmy', 'Jennifer', 'Jason']
##new_users = ['John', 'Johnny', 'john', 'Jack', "Ryan"]
##for user in new_users:
##    if ((user.upper() or user.lower()) in current_users):
##        print "Sorry %s username has been taken!\n" %user
##        break
##    else:
##        print "Congratulations those usernames are available!"
##


###Checks if list is empty or not!
##admin = []
##if admin:
##    print "Users are there!"
##else:
##    print "Missing users!"
####for user in admin:
####    if user == "admin":
####        print "Hello admin, would you like to see a status report?"
####        break
####    else:
####        print "Hello Eric, thank you for logging in!"
####age = 29
####if (age) < 2:
####    print "You are a baby!\n"
####elif (age >= 2) and (age < 4):
####    print "You are a toddler!"
####elif (age >= 4) and (age < 13):
####    print "You are a kid!"
####elif (age >= 13) and (age < 20):
####    print "You are a teenager!"
####elif (age >= 20) and (age < 65):
##    print "You are an adult!"
##elif (age > 65):
##    print "You are a senior citizen!"
####
##fruits = ['kiwi', 'lemon', 'lime', 'tomato', 'watermelon']
##for fruit in fruits:
##    if fruit == 'watermelon':
##        print "You must love watermelons!"
##sentence = " The grass is greener on the other side of the road! "
##print sentence.lstrip()
##print sentence.rstrip()
##print sentence.strip()
##print sentence.title()
##print sentence.upper()
##print sentence.lower()
###print the first 5 numbers!
##for x in range(1,6,1):
##    print x

####Loop basics
##
##import random
##
###Prints numbers 5 thru 0
##i = 5
##while True:
##    print(i)
##    i = i - 1
##    if i == 0:
##        print("end of loop!")
##        break
##    
####    
#####Prints even numbers
####x = 0
####while True:
####    print(x)
####    x = x + 2
####    if x > 10:
####        break
####
#####Break statement, breaks loop AS SOON as n is equal to 6
#####Outputs 0 thru 5!
####n = 0
####while True:
####    print(n)
####    n = n + 1
####    if n >= 6:
####        print("It's over!")
####        break
####
####Continue statement stops the current iteration and moves on to the next
##
##c = 0
##while True:
##    print(c)
##    c = c + 1
##    if c == 2:
##        continue
##        print("Skipping 2!")
##        ##Ex: using continue skips 2 and moves on to next ones!
##    
##    if c == 5:
##        print("Break loop!")
##        break

###Lists!
##nums = [10,9,8,7,6,5]
###Reassigns first element in nums
##nums[0] = nums[1] - 5
##if 4 in nums:
##    print(nums[3])
##else:
##    print(nums[2])

#IF i in range 0 thru 10 is divisible by 2, add it to 1
##for i in range(1,11):
####    print i
##    if i % 2 == 0:
##        print(i + 1)
               
#####Using for loop to iterate thru list!
##letters = ["a", "b", "c", "w", "x", "Y", "Z"]
###print(letters)
##for x in (letters):
##    print(x + "!"),

##
####Print 1 random numbers from 1 through 30
####Need to import random first!!
##import random
##
##for i in range(1):
##    number = random.randint(1,30)
##    print(number)

##Using for loop to iterate pairs (definitions) from a dictionary
##webster = {"Aardvark: " : "A star of a popular children's cartoon show.", "Baa: " : "The sound a goat makes.",
##           "Carpet: ": "Goes on the floor.", "Dab: ": "A small amount."}
##
##for word in webster:
##  print word, webster[word]


##prices = {"banana" : 4, "apple" : 2, "orange" : 1.5, "pear" : 3}
##
##stock = {"banana" : 6, "apple" : 0, "orange" : 32, "pear" : 15}
##
##for value in stock:
##    print value
##total = 0
##for value in prices:
##    amount = prices[value] * stock[value]
##    total = total + amount
##print (total)


  
    
