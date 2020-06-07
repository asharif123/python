
from time import sleep


#create a function to take the average of numbers in a list
def average(numbers):
  length = len(numbers)
  i = 0
  total = 0
  while i < length:
    total = total + numbers[i]
    i = i + 1
  average = (float(total)/length)
  print (round(average, 3))

##countries = {}
##while True:
##  name = input("Please enter your name: ")
##  country = input("Name a country you would like to visit: ")
##  countries[name] = country
##  response = input("Would you like to continue (Y/N) ").upper()
##  if response == "N":
##    print "Exiting the program.."
##    break
##
##for first_name, land in countries.items():
##  print "\n%s wants to go to %s." %(first_name, land)
##  sleep(1)
##  for value in pupil["quizzes"]:
##    quiz_total = 0 + value
##  total_score = quiz_total + homework_total + pupil["final_exam"]
##  print ("%s's total quiz score of the class is %s." + "\n") %(pupil["name"], quiz_total)
##
##  print ("%s scored a %s on the final exam!" + "\n") %(pupil["name"], pupil["final_exam"])
##
##  print ("%s's total score in the class is %s.m" + "\n") %(pupil["name"], total_score)
##  
##
##
##
#######dictionary loops
####import math
######create the 'sum' function that takes the sum of all numbers in a list!
##
def sum(numbers):
  total = 0
  numbers = list(numbers)
  for number in numbers:
    total = total + number
  print (total)
  
students = ({
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0 ,92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
},
{
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
},
{
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
})


##Calculate average score

for student in students:
  homework_score = sum(student["homework"])
  quizzes_score = sum(student["quizzes"])
  tests_score = sum(student["tests"])

  print (type(int(homework_score)))
  

