##Asks user for password, must get it in 3 guesses!

##guess = 3
##while guess > 0:
##    password = str(raw_input("Please enter your password: "))
##    if (password == "Allah123!"):
##        print ("You have logged in! \n")
##        break
##    else:
##        print ("Please try again! \n")
##        guess = guess - 1
##    if (guess == 0):
##        print ("Sorry, you entered the wrong password 3 times, resetting!")
##        guess == 3
##        password = str(raw_input("Please enter your password: "))

##infinite login attempts!
while True:
    password = str(input("please enter your password: "))
    if (password == 'Allah123'):
        print "You have logged in!" + "\n"
        break
    else:
        print "Please try again!" + "\n"
        
