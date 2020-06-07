##Roll a pair of dice, add values of roll
#User guesses a number
# If user's guess is greater than total of dice roll, they win!

import random

from time import sleep


user_guess = int(raw_input("Please enter a number: "))
  
first_roll = random.randint(1, 6)
second_roll = random.randint(1, 6)
  
  
sleep(1)
#user_guess = get_user_guess()
  
if user_guess >= 12:
  print("Invalid number! Terminating program!")

else:
  print ("Rolling: ")
  sleep(2)
  print ("Number of first dice is %d") %(first_roll)
  print ("Number of second dice is %d") %(second_roll)
    
  total_roll = first_roll + second_roll
  print("Result...")
  sleep(1)
    
  if user_guess > total_roll:
    print("You are a winner!")
  elif user_guess < total_roll:
    print("You lost!")
      
  print(total_roll)

    
                                            
    
    
    
  
  
  
  
  
  
  



