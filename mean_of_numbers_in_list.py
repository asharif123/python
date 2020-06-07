 #####Finding the mean of numbers in a bracket#####

##If number of elements is odd, median is the middle number
##If number of elements is even, median is the average of middle 2 numbers

def median(numbers):
  numbers = list(numbers)
#Takes numbers in a list and puts them in numerical order!!
  numbers = sorted(numbers)
  #numbers = list(numbers)
  length = len(numbers)
  if length == 1:
    print numbers[0]
  

###If there is only 1 number in a list, median is just that number!  
##  for value in numbers:
##    if length == 1:
##    	return value
###If number of elements is even    
##    elif ((length) % 2 == 0):
##      total = (numbers[(length/2)] + numbers[((length/2) - 1)])
##      average = (float(total) / 2)
##
###If number of elements is odd    
##    else:
##      average = numbers[(length - 1) / 2]
##      
##  return average
