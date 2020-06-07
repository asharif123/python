####### Dictionary basics (using brackets!) ######
##person = {'first_name': 'Awad', 'last_name': 'Sharif', 'age': 28,
##          'city': 'Mountain View'}
##print person
##name = str(raw_input("Please enter Jack, Awad or Mike: "))

place_1 = {"name": "AWAD", "places": ["Japan", "China", "Uzbekistan"]}
place_2 = {"name": "RECEP", "places": ["Turkey", "Tunisia", "Kyrgstan"]}
place_3 = {"name": "JONATHAN", "places": ["Nigeria", "Oman", "Russia"]}
places = [place_1, place_2, place_3]
##i = 0
##while True:
##  name = str(input("Enter AWAD, JONATHAN, RECEP, X to exit: ")).upper()
##  if name == "X":
##      print ("Exiting program")
##      break
###if name exists in the places, print out the places that the person would like to visit!!
##  else:
##    for place in places:
##      if place["name"] == name:
##        print (place["name"] + " likes to visit: " + place["places"][0] + ", " + place["places"][1] + ", " + "and " + place["places"][2] + ".\n")
##        
##      
    
      
      
##    else:
##      print "Name does not exist in dictionary!"
##    
##  if name in places["name"]:
##    print place["places"]
  ##pet = [pet_1, pet_2, pet_3, pet_4, pet_5, pet_6]
##
##for name in pet:
##  print "The type of pet is a %s and the owner's name is %s" %(name["pet"], name["owner"]) + "\n"

first_person = {'name': 'Awad', 'age': 29, 'occupation': 'Mobile Tester'}
second_person = {'name': 'Arif', 'age': 63, 'occupation': 'Car Salesman'}
third_person = {'name': 'Talat', 'age': 53, 'occupation': 'Coding Manager'}

person = [first_person, second_person, third_person]

for individual in person:
  print ("The person's name is " + individual["name"] + ", whose age is " + str(individual["age"]) + " and has the occupation as a " + individual["occupation"] + "." + "\n")

##rivers = {'nile': 'Egypt', 'Lake Michigan': 'Michigan', 'Lake Ohio': 'Ohio'}
##for river, country in rivers.items():
##  print ("The " + river + " river is located in " + country + "." + "

##food = {'pizza': 'deep dish', 'toppings': ['mushrooms', 'olives']}
##for toppings in food['toppings']:
##  (print "You ordered a " + food['pizza'] + " with " + toppings + "." + "\n")

alien_1 = {'color': 'green', 'points': 5}
alien_2 = {'color': 'red', 'points': 10}
alien_3 = {'color': 'blue', 'points': 15}
print (alien_1.keys())
aliens = []
for i in range(30):
  aliens.append(alien_1)
  if alien_1['color'] == 'green':
    alien_1['color'] = 'red'
print (aliens)
##print aliens(len(numbers_list)/2)
##
####for i in range(30):
####  aliens.append(alien_1)
####print aliens[0:4]
##
####aliens = [alien_1, alien_2, alien_3]
####for alien in aliens:
####  print ("The color of the alien is " + alien['color'] + " and it's worth " + str(alien['points']) + "\n")
##
##
###.items() returns a list of key and pairs!
##glossary = {'.title': 'Capitalizes first letter in each word',
##            '.upper': 'capitalizes every letter',
##            '.lower': 'lowercases every letter',
##            '.strip': 'gets rid of whitespace',
##            '.sorted': 'puts words in order'}
##for word, definition in glossary.items():
##  print (word + ': ' + definition + '\n')
####for word, definition in glossary.items():
####  print (word + ': ' + definition + '\n')
##
##
####
#####loop thru all the keys in the glossary
####for name in glossary.keys():
##  print name + '\n'

##alien_position = {'x_coordinate':25, 'y_coordinate':35, 'speed':'medium'}
##print ("Original position = %s, %s") %(alien_position['x_coordinate'], alien_position['y_coordinate'])
##if alien_position['speed'] == 'slow':
##  x_increment = 1
##elif alien_position['speed'] == 'medium':
##  x_increment = 2
##elif alien_position['speed'] == 'fast':
##  x_increment = 3
##alien_position['speed'] = alien_position['x_coordinate'] + x_increment
##print alien_position

##alien_0 = {'color': 'green', 'points':56}
##for key in alien_0:
##  print key, alien_0[key]
##
###adding elements to alien_0
##alien_0['x_coordinates'] = 25
##alien_0['y_coordinates'] = 35
###modify an element
##alien_0['x_coordinates'] = 45
##print alien_0

##print the pair
##print alien_0['color']

##ages = {"Awad":27, "Urooj":25, "Dad":61, "Mom":52, "Farihah":23}
##
###Print dictionary and keys inside dictioary
##for info in ages:
##  print info, ages[info]
### Assigning stuff to dictionary ####
##squares = {2:3,1:1,4:3,3:'error',4:16}
##
###This new entry gets assigned at the beginning
##squares[8] = 64
##
###This gets reassigned 
##squares[3] = 9
##print(squares)
##
####Get information in dictionary
##print(squares.get(2))
##print(squares.get(3))
##
###Since 9 is NOT in squares dict, value after 9 is used and added to value assigned to 2
##print(squares.get(2) + squares.get(9,7))
##
##
##### Tuple basics #####
##words = ("spam", "eggs", "sausages")
##print(words[0:])
##
sqs = [1,3,5,12,11,14,15,2,9]
###print first 6 elements
##print(sqs[0:6])
##
###prints 1, 5, 11 15, and 9
##print(sqs[::2])
##
#prints elements in reverse order
print(sqs[::-1])
##
#####prints all values
##print(sqs[0:])
##
###prints second to last value
##print(sqs[7:-1])
##
def censor(sentence, word):
  #sentence = sentence.split()
  for value in sentence.split():
    #print (value)
    if (word == value):
      new_sentence = sentence.replace(word, ("*" * len(word)))
  print (new_sentence)
      
      
    





