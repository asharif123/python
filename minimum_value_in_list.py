##def minimum_value(values):
##    ##ex: [54,6,75]
##    start_value = values[0]
##    for i in range(1,len(values)):
##        if start_value < values[i]:
##            start_value = start_value
##        else:
##            start_value = values[i]
##    return start_value
##print(minimum_value([15,114,12,21,43]))
##
##def maximum_value(values):
##    start_value = values[0]
##    for i in range(1,len(values)):
##        if start_value > values[i]:
##            start_value = start_value
##        else:
##            start_value = values[i]
##    return start_value
##
##def reverse_number(number):
##    if type(number) != int:
##        return "Please enter a positive or negative integer!"
##    if number > 0:
##        number = str(number)
##        return int(number[::-1])
##    if number < 0:
##        number = str(number)
##        number = list(number)
##        number = number[::-1]
##        number.pop(-1)
##        number.insert(0,'-')
##        return int(''.join(number))
##print(reverse_number(-1124214122))
##print(1 // 10)
def convert_to_single_digit(values):
##ex: 12345678 -> 36 -> 9
    total = 0
    while values > 0:
        value = values % 10
        total += value
        values //= 10
        if values == 0 and total > 9:
            values,total = total,0
    return total
print(convert_to_single_digit(321))
        

