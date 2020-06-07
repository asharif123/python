##countdown
def countdown(value):
    values = []
    for i in range(value,-1,-1):
        values.append(i)
    return values
print(countdown(5))

##print and return
def print_and_return(values):
        print(values[0])
        return values[1]
print(print_and_return([1,2]))

##return sum of first number and length of numbers
def first_plus_length(values):
    return values[0] + len(values)
print(first_plus_length([17,2,3,4,5,14,22,24]))

def values_greater_than_second(values):
    greater_than_second = []
    for i in range(len(values)):
        if (values[i] > values[1]):
            greater_than_second.append(values[i])
    
    if len(greater_than_second) < 2:
        return False
    print(len(greater_than_second))
    return greater_than_second

print(values_greater_than_second([5,2,3,2,1,4]))

def length_value(size,value):
    duplicates = []
    for i in range(size):
        duplicates.append(value)
    return duplicates
print(length_value(4,7))
