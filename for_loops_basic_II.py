##biggie size
def biggie_size(values):
    for i in range(len(values)):
        if (values[i] > 0):
            values[i] = "big"
    return values

print(biggie_size([-1,3,5,-5]))

def count_positives(numbers_list):
    total = 0
    for i in range(len(numbers_list)):
        if (numbers_list[i] > 0):
            total += 1
    numbers_list[-1] = total
    return numbers_list

print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

def sum_total(values):
    total = 0
    for i in range(len(values)):
        total += values[i]
    return total

print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

def average(list_values):
    total = 0
    for i in range(len(list_values)):
        total += list_values[i]
    return float(total) / len(list_values)

print(average([1,2,3,4]))


##return the length of a list 
def length(list_values):
    count = 0
    for value in list_values:
        count += 1
    return count
print(length([3,2,1,-9]))
## takes a list of numbers and returns the minimum value in the list
##return False if empty list

def minimum(list_values):
    if len(list_values) == 0:
        return False
    else:
        min_value = list_values[0]
        for i in range(1,len(list_values)):
            if (list_values[i] < min_value):
                min_value = list_values[i]
        return min_value
print(minimum([37,2,1,-9]))

def maximum(list_values):
    if len(list_values) == 0:
        return False
    else:
        max_value = list_values[0]
        for i in range(1,len(list_values)):
            if max_value < list_values[i]:
                max_value = list_values[i]
        return max_value
print(maximum([2,1,37,53,-9,2,4,14,52]))

##returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.

def ultimate_analysis(values):
    if len(values) == 0:
        return False
    max_value = maximum(values)
    min_value = minimum(values)
    length = len(values)
    sum_values = sum_total(values)
    average_values = average(values)
    return {'sumTotal': sum_values, 'average': average_values, 'minimum': min_value, 'maximum': max_value, 'length': length}
print(ultimate_analysis([37,2,1,-9]))

##reverse a list of numbers WITHOUT creating a new list
##Ex: [37,2,1,-9] -> [-9,1,2,37]
##[-9,2,1,37]
##[-9,1,2,37]
##ex: [1,2,3,4,5]
##[5,2,3,4,1]
##[5,4,3,2,1]
def reverse_numbers(numbers_list):
    length = int(len(numbers_list)/2)
    for i in range(length):
        temp = numbers_list[i]
        numbers_list[i] = numbers_list[len(numbers_list)-1-i]
        numbers_list[len(numbers_list)-1-i] = temp
    return numbers_list
print(reverse_numbers([37,2,1,9]))
print(reverse_numbers([4,8,15,16,23,42]))
    
    
    
        
