#user enter a number
#iterate thru each digit in the enteted number
#NOTE: CANNOT ITERATE VIA AN INTEGER!)
#convert each digit to 'seven_digit' representation
##take each converted digit and print line=by=line
##do same for other digits

representations = {'0': ['###', '# #', '# #', '# #', '###'],
                   '1': ['#','#','#','#','#'],
                   '2': ['###','  #','###','#  ','###'],
                   '3': ['###','  #','###','  #','###'],
                   '4': ['# #','# #','###','  #','  #'],
                   '5': ['###','#  ','###','  #','###'],
                   '6': ['###','#  ','###','# #','###'],
                   '7': ['###','  #','  #','  #','  #'],
                   '8': ['###','# #','###','# #','###'],
                   '9': ['###','# #','###','  #','###']}

def convert_digit_to_seven_digits(number):
    number = str(number)
    seven_digits = [representations[value] for value in number]
    for i in range(5):
        print(' '.join(value[i] for value in seven_digits))
convert_digit_to_seven_digits(1234567890)


















    
##    ##combine each index in each value as one list, and join together
##    for i in range(5):
##        print (' '.join([seven_digits[j][i] for j in range(len(seven_digits))]))
##convert_digit_to_seven_digits(10)









    
##    number = str(number)
##    converted_digits = [representations[digit] for digit in number]
##    for i in range(5):
###take each individual list from converted_digits
###print out each element of ind list in diff lines until range(5)
###move to next digit and print in top line using for segment in converted_digits
###.join is used to join together different digits
##        print (' '.join(segment[i] for segment in converted_digits))
##(convert_digit_to_seven_digits(1234567890))
##
    
