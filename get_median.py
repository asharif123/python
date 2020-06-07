##Get the median from a list of numbers!
##if length is odd, median is the middle
##if even, median is avg of 2 middle numbers!
def get_median(*numbers):
    numbers = sorted(numbers)
    length = len(numbers)
    
    if length == 1:
        print numbers
    elif (length % 2) == 0:
        value = float(numbers[length/2] + numbers[(length/2)-1])/2
        print(value)
    elif (length % 2) != 0:
        value = numbers[(length-1)/2] 
        print float(value)
#1,4,5,6,7.3,8
get_median(1,8,4,7.3,5,6,)
