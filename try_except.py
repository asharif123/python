####try and except!

#ValueError - raised when wrong input is inputted (ex: enter a string to input that ONLY takes integers/floats)
#TypeError - adding/subtracting/dividing 2 of diff types!
#ZeroDivisionError
#OverflowError - raised when large value is outputted
#IndexError 
#KeyboardInterrupt
#MemoryError - code fails to run due to lack of memory
#KeyError - no key exists in dictioary
dictionary = { 'a' : 'b', 'b' : 'c', 'c' : 'd' }
value = 'a'
try:
    while True:
        value = dictionary[value]
        print (value)
except KeyError:
    print ("DNE!")
    

def readint(minimum, maximum):
 
    while True:
        try:
            value = int(input("Enter a number from " + str(minimum) + " " + "to" + " " + str(maximum) + ": "))
            if value in range(minimum, maximum+1):
                return ("\nThe value is " + str(value) + ".")
            else:
                print ("\nError: the value is not within permitted range (" + str(minimum) + "..." + str(maximum) + ")\n")
        except ValueError:
            print ("\nError: wrong input\n")
v = readint(-10, 10)
print(v)
##while True:            
##    try:
##
##       print("\nThe number is:", v)
##       break
##    except ValueError:
##        print ("Error: wrong input")
 
##try:
##    print("1")
##    x = 1 / 0
##    print("2")
##except:
##    print("Oh dear, something went wrong...")

##print("3")
##
###use raise to raise exception elsewhere
###raise MUST be used with except block only!
def badFun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise

import math
#assert is used to ensure no wrong data is raised
#AssertionError is raised if assert condition is violated!
#ex: assert that x value is greater than 0!
x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)
##
##try:
##    badFun(0)
##except ArithmeticError:
##    print("I see!")
##
##print("THE END.")

##firstNumber = int(input("Enter the first number: "))
##secondNumber = int(input("Enter the second number: "))
###calculation not performed if any errors are raised.
##try:
##    print(firstNumber / secondNumber)
##except:
##    print("This operation cannot be done.")
##
##print("THE END.")

import os
##os.chdir('C:/Users/Awad/Documents')
##print (os.getcwd())
##while True:
##    try:
##        first_number = float(input('Please enter a number: '))
##        second_number = float(input('Please enter a second number: '))
##        result = (second_number) / (first_number)
##        return result
##    except ZeroDivisionError:
##        print ("Can't divide by zero dude!\n")
##
##    else:
##        print (round((result),3))
##        break

##while True:
##    first_number = (input("Please enter the first number: "))
##    second_number = (input("Please enter the second number: "))
##    if (first_number == "q") or (second_number == "q"):
##        break
##    try:
##        total = float(first_number)/ (float(second_number))
##
##    except ZeroDivisionError:
####Raise an exception if number is divided by 0!
##        print ("\nYou cannot divide value by zero man!!\n")
###IF there is no zero division error, print out the result!
##    else:
##        print (total)

##try:
##    with open('filename.txt') as filename:
##        read_file = filename.readlines()
##        for row in read_file:
##            print row
##
##except FileNotFoundError:
##    print "Sorry could not open the file!"

##try:
##    first_value = int(raw_input("Please enter a number: "))
##
##except ValueError:
##    print "You did not enter an integer!"
##
##else:
##    print first_value
##
####
####COUNT THE TOTAL NUMBER OF WORDS IN A FILE!
##import os
##os.chdir('C:/Users/Awad/Desktop')
##print (os.getcwd())
##filename = 'learning_python.txt'
##
##total = 0
##try:
##    with open('learning_python.txt') as filename:
##        read_file = filename.readlines()
##        print (read_file)
##except ZeroDivisionError: 
##    print ("Cannot open file!")
##
##else:
##    for line in read_file:
##        line = line.split(' ')
##        for word in line:
##            total += 1
##    print ("Total words: " + str(total))

##raise 'FileNotFoundError' if you open a file that doesn't exist!
##try:
##    with open('file.txt') as filename:
##        file_read = filename.readlines()
##except FileNotFoundError:
##    print ("ERROR! ERROR!\n")
##else:
##    print (file_read)

#Test ValueError
##while True:
##    try:
##        first_value = int(input('Please enter a value: '))
##        second_value = int(input("Enter another value: "))
##    except ValueError:
##        print ("Invalid entry!\ni")
##    else:
##        print (first_value + second_value)
##        break
        
        
    
        
