############## Functions #######
##def greetings(name):
##    print ("Hello my name is " + name)
##greetings("Awad")
##
def car_information(make,model,**other_info):
    
#use double asterisks to create a dictionary as an argument
#more_info takes as much info about car and stores it in a more_info dictionary
#store all information in a dictionary!
    car_info = {}
    car_info['make'] = make
    car_info['model'] = model
    #car_info['other_info'] = other_info
    car_info['other_info'] = other_info
    print (car_info)
car_information('Buick','Verrano',year='2014',color='green',price='22000')
car_information('Chevy','Trailblazer',color='red',MPG='22.5')
##def sandwiches(*items):
####    print "You want the following in your sandwich: " + "\n"
####    for item in items:
####        print item + "\n"
####    
##
#####USE ASTERISK BEFORE ARGUMENT to accept infinite arguments!
####def make_pizza(size, *toppings):
####    print "You would like to order a size %s pizza with these toppings: " %(size)
####    for topping in toppings:
####        print topping
####    
####
########def favorite_book(title):
########    print "My favorite book is %s." %(title.title())
########
########favorite_book("Harry Potter: And the Chamber of Secrets")
######
######def make_shirt(size, text):
######    print "\nI would like to get a %s size T-Shirt." %(size)
####    print "\nI would like the T-Shirt to say '%s'!" %(text)
####
##
###age is default argument, meaning don't need to enter it in person
####person = {}
######def person(first_name, last_name, age=''):
####while True:
####    first_name = input("Enter your first name: ")
####    last_name = input("Enter your last name: ")
####    age = int(input("enter your age: ")    
##    
###Make the middle_name optional to input by assigned it to ' '
##def full_name(first_name, last_name, middle_name=''):
##    full_name = first_name + " " + middle_name + " " + last_name
##    print full_name
##
######def describe_city(city, country):
######    print city, country
######    return city, country
####
##def animal(animal_type,name=''):
##    print "The type of animal you have is a %s" %(animal_type)
####
####
def is_it_prime(number):
    if number < 1:
        print ("Invalid entry!")

    elif number == 2:
        print ("2 is a prime number!")

    else:
        for x in range(2,number):
            if (number % (x)) == 0:
                return False
              
        

    return True



########
########def even(x):
########    if (x % 2) == 0:
########        print("%s is an even number!") %(x)
########    else:
########        print("%s is an odd number!") %(x)
########
########
##########Functions using returns
##########Return uses a value that can be used later!
########
########def add_numbers(x,y):
########    return (x + y)
########
########
########
########def exclamation(word):
########    print(word + "!")
########
########
########def list_function(n):
########    n[1] = n[1] + 3
########    print n
########
########n = [3, 5, 7]
#########print list_function(n)
########
########n = [3, 5, 7]
########
######def double_list(n):
######    value = []
######    for i in n:
######        number = i*2
######        value.append(number)
######    print value
######  
####### Don't forget to return your new list!
######
########print double_list(n)
########
########
########## Takes strings from a list and combines them together!
########def join_strings(words):
########
#########empty string where words are added to combine them!
########  result = ""
########  for item in words:
########    result = result + item
########  print result
########
############join 2 lists together
########m = [1, 2, 3]
########n = [4, 5, 6]
########
########
########def join_lists(x,y):
########  results = x + y
########  return results
########print join_lists(m, n)
########
########
##########Concatenate 2 lists together
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(n):
    #empty string to put 2 lists into!
    values = [value for line in n for value in line]
    return values
print (flatten(n))

##########function to see if number is even
########def is_even(x):
########  if (x % 2) == 0:
########    return True
########  else:
########    return False
########Takes digits in number and adds them (Ex, 437 = 14)
##def digit_sum(n):
##    #n = int(input("Please enter an integer greater than 0: "))
##    total = 0
##    if n > 0:
##        n = str(n)
##        for value in n:
##            total = total + int(value)
##        return total
##
######    
########
##########Take factorial of numbers
##########Ex: factorial(2) = 2*factorial(1) = 2
##########factorial(3) = 3*factorial(2) = 3*2 = 6
##########factorial(4) = 4*factorial(3) = 4*6 = 24
##def factorial(x):
##  if (x == 1) or (x == 0):
##    return 1
##  elif x > 1:
##    return x * factorial(x-1)
##  elif x < 0:
##    return "Invalid entry!"

################Determines if a number is prime##############
######
def is_prime(x):
    if x <= 1:
        return False
#if x is greater than 1, start evaluating if it's prime or not!
    elif x > 1:
        for n in range(2, x-1):
#if x is evenly divisible by any number in range, return False
#return True runs if x IS a prime number and fails if condition
#else: adds another condition to check if x is NOT divisible 
#Ex: using else, if (x % n) != 0, return True
#w/o else, loop sees if ANY value in range 2 to x-1 goes evenly in x
#using else mean if ANY # in range IS not divisible to x
#ex: 9 % 2 != 0, so would jump to else cond and make it prime!!
            if (x % n) == 0:
                return False
#return True if n is a prime number and fails if cond!!!
        return True
            
            

            

#####this strips brackets, quotes, and commas from split list
######    sentence =' '.join(sentence)
####
####    print sentence
####    
def count(sequence, item):
  sequence = sequence.split()
  #print sequence
  count = 0
  item = item.lower()
  for entry in sequence:
    if entry == item:
      count = count + 1
  print (count)
      
