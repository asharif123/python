grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

#Returns the sum of values in a list!
#Function was created manually!
def grades_sum(scores):
  total = 0
  for score in scores: 
    total = total + score
  return total
#call the function on "grades" list!
print grades_sum(grades)

def grades_average(grades_input):
  sum_of_grades = grades_sum(grades)
  average = sum_of_grades / float(len(grades_input))
  return average
print grades_average(grades)

def grades_variance(grades):
    variance = 0
    for number in grades:
#Take the variance of each and add to 0 to get variance of all numbers!
        variance = (variance) + (grades_average(grades) - number) ** 2
    return variance / len(grades)
print grades_variance(grades)

###take the square root of variance!
##def grades_std_deviation(variance):
##  variance ** 0.5
##  return variance
##print grades_std_deviation(grades)

#variance = grades_variance(grades)

##for grade in grades:
##  print grade


