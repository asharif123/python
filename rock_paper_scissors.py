###User selects rock, paper, or scissor
###Computer selects rock, paper, or scissor
###Inform if user or computer wins

import random
from time import sleep

print "Welcome to Rock, Paper, Scisscors!"
sleep(2)
print "Select R for Rock, P for Paper, or S for Scissors!"


options = ["R", "P", "S"]
number = random.randint(0,2)
computer_option = options[number]
user = str(raw_input("Select R for Rock, P for Paper, or S for Scissors: "))
if user in options:
    user_option = options.index(user)

print computer_option
print user_option
##LOSER_MESSAGE = "You lost!"
##WINNER_MESSAGE = "Congratulations, you won!"
##
##def decide_winner(user_choice):
##    print "You selected %s" %(user_choice)
##    print "Computer selecting..."
##    sleep(1)
##    computer_choice = random.randint(1,3)
##    print "Computer selected %s" %(computer_choice)
##
## #user input is indexed against the options list,
## #if it exists, index of input is printed out from list
##    user_choice_index = options.index(user_choice)
##    computer_choice_index = options[computer_choice]
##    print (user_choice_index)
##    print (computer_choice_index)
##
#### WINNING SCENARIOS
##    if user_choice_index == computer_choice_index:
##        print "Tie game!"
##    elif (user_choice_index == 1 and computer_choice_index == 0):  
##        print WINNER_MESSAGE
##    elif (user_choice_index == 2 and computer_choice_index == 1):
##        print WINNER_MESSAGE
##    elif (user_choice_index == 0 and computer_choice_index == 2):
##        print WINNER_MESSAGE
##
#### LOSING SCENARIOS   
##    elif (user_choice_index == 0 and computer_choice_index == 1):  
##        print LOSER_MESSAGE
##    elif (user_choice_index == 1 and computer_choice_index == 2):
##        print LOSER_MESSAGE
##    elif (user_choice_index == 2 and computer_choice_index == 0):
##        print LOSER_MESSAGE
##        
##    elif (user_choice_index > 2 or user_choice_index > 2):
##        print ("Invalid input! Index must be 0, 1, or 2!")
##        #exit the loop if invalid option
##        break
##   
##
