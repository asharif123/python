### User selects shape and program calculates area 
#User selects shape, calculate and print area of shape

##import pi to calculate area of circle
from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
#print("Program for calculating shapes has begun!\n")

#Print current time and day
print(str(now.month) + '/' + str(now.day) + '/' + str(now.year) + " " + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second))

#Ask the program to sleep for 1 second
sleep(1)


while True:
  #User enters shape automatically becomes uppercase
  option = str(input("Enter C for Circle, T for Triangle, or X to exit the game: ")).upper()
  
  if option == 'C':
    #Convert string to float since raw_input only takes string
    radius = float(raw_input("Enter the radius: "))
    area = pi*(radius)**2
    sleep(1)
    #print the area to 2 significant digits
    print('Area: %.2f \n') %(area)
    
  elif option == 'T':
    base = float(raw_input("Enter base: "))
    height = float(raw_input("Enter height: "))
    area = 0.5 * base * height
    print("Area: %.2f \n") %(area)

  elif option == "X":
    print ("You have exited the game!")
    break
    
  else:
    print("\nInvalid option you idiot!\n")
