#print("Twinkle, twinkle, little star,")
#print("\t\tHow I wonder what you are!")
#print("\t\t\tUp above the world so high,")
#print("\t\t\tLike a fdiamond in the sky.")
#rint("Twinkle, twinkle, little star,")
#print("\t\tHow I wonder what you are!")
import math
#print python version and info
import sys
print(sys.version)
print(sys.version_info)

#print current date and time
from datetime import datetime
print('Current date and time: ')
now = datetime.now()
print(now)


##
##
####string practice
###Enter the radius and get area
##from math import pi
##radius = float(input("Enter the radius: "))
##area = round((pi*(radius**2)),3)
##print ("Area: " + (str(area)))

##accepts a sequence of numbers and prints list/tuple
def numbers_to_list(*numbers):
    numbered_list = []
    for number in numbers:
        numbered_list.append(str(number))
    tuple_list = tuple(numbered_list)
    print('List: ' + str(numbered_list))
    print('Tuple: ' + str(tuple_list))

##accept file name and print out extension
##filename = str(input("Enter a filename: "))
##filename = filename.split('.')
####print(filename[1])
##
###display first and last color from color list
##color_list = ['Red','Green','White','Blue']
##print(color_list[0],color_list[-1])

##print exam date
exam_st_date = (11,12,2014)
print('The examination will start from: ' + ' ' + str(exam_st_date[0]) + ' ' +'/' + ' ' + str(exam_st_date[1]) + ' ' + '/' + ' ' + str(exam_st_date[2]))

##take a number and print as n + nn + nnn

##a = int(input("Input an integer : "))
##n1 = int( "%s" % (a) )
##n2 = int( "%s%s" % (a,a) )
##n3 = int( "%s%s%s" % (a,a,a) )
##
##print (n1+n2+n3)

##print calendar of current month and year
import calendar
#calendar.month(year,month)
print(calendar.month(2020,1))

print("a string that you \"don\'t\" have to escape")
print("This")
print("is a ....... multi-line")
print("heredoc string --------> example")

##count total days
from datetime import date
current_date = date(2014,1,2)
next_date = date(2015,7,11)
total_days = next_date - current_date
print(total_days.days)

##print volume of sphere
##from math import pi
##radius = float(input("Enter a radius: "))
##volume = (4/3)*pi*(radius**3)

##is_string
def is_sentence(sentence):
    sentence = sentence.capitalize()
    if sentence[0:2] == "Is":
        return sentence
    else:
        sentence = "Is" + " " + sentence
        return sentence
#print(is_sentence('is world'))

def count_4(numbered_list):
    total = 0
    for value in numbered_list:
        if value == 4:
            total += 1
    return total

def copies_of_first_two(sentence,n):
    two_characters = sentence[0:2]
    if len(sentence) < 2:
        return sentence*n
    else:
        return n*two_characters

def is_vowel(letter):
    letter = letter.lower()
    if letter in 'aeiou':
        return True
    else:
        return False
def histogram(items):
    for n in items:
        output = ' '
        times = n
        while(times > 0):
            output += '*'
            times = times - 1
    print(output)
histogram([2,3,6,5])

values = ['hello','welcome','to','python']
str_values = ''
for value in values:
    str_values += value + ' '


def print_even(numbers):
    for value in numbers:
        if (value % 2) == 0:
            print(value)
        if value == 237:
            print(value)
            break
print_even(numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ])

colors_1 = set(['White','Black','Red'])
colors_2 = set(['Red','Green'])
#.difference prints elements from first set that are NOT in second set
colors_3 = colors_1.difference(colors_2)
print(colors_1 - colors_2)

####greatest common factor
##def GCF(value_1,value_2):
##    if value_1 < 0 or value_2 < 0:
##        return "Enter a positive integer!"
##    factors_1,factors_2 = [],[]
##    elif value_1 == 0 or value_2 == 0:
##        return 0
##    for value in range(1,value_1+1):
##        if (value_1 % value) == 0:
##            factors_1.append(value)
##    for value in range(1,value_2+1):
##        if (value_2 % value) == 0:
##            factors_2.append(value)
##    common_factors = []
##    for value in factors_1:
##        if value in factors_2:
##            common_factors.append(value)
##    return max(common_factors)
def gcf(x,y):
    if x == 0 or y == 0:
        return 0
    if x == y:
        return x
    for value in range(int(y/2),0,-1):
        if (x % value) == 0 and (y % value) == 0:
            return value
print(gcf(12,24))
##least common multiple
def LCM(value_1,value_2):
    if value_1 == value_2:
        return value_1
    if value_1 == 0 or value_2 == 0:
        return 0
    first_values,second_values = [],[]
    for value in range(1,value_2+1):
        first_values.append(value_1*value)
        second_values.append(value_2*value)
    for value in first_values:
        if value in second_values:
            return value
print(LCM(0,5))
##15: 15,30,45,60,75
##25: 25,50,75

##def square(x,y):
##    return ((x+y)*(x+y))
##
####compute future value of specified principal amount
##amt = 1000
##interest = 3.5
##years = 7
##principal_amount = amt*((1+(0.01*interest)) ** years)
##
##def distance(x1,y1,x2,y2):
##    return ((x2-x1)**2 + (y2-y1)**2)**0.5
##print(distance(4,0,6,6))

##check whether file exists in OS directory
import os
#open('abc.txt','w')
print(os.path.isfile('afsdfsddsbc.txt'))
##print(os.path.isdir())
##print os name, platform, release name
##import platform
##print(os.name)
##print(platform.system)
##print(platform.release)
##
###Locate python site-packages
##import site
##print(site.getsitepackages())

###call an external command to python
##from subprocess import call
##call(["ls","-l"])


##print a string without whitespace (end-'') or newline print('\n')
for i in range(10):
    print(str(i),end='')
print('\n')

##get username
import getpass
print(getpass.getuser())

##get sum of first n positive integers
def sum_of_n_integers(integers,n):
    total = 0
    for i in range(0,n):
        total += integers[i]
    return total
print(sum_of_n_integers([1,2,3,4,5],3))

n = int(input("Input a number: "))
2
sum_num = (n * (n + 1)) / 2
3
print(sum_num)

##convert height in inches to cm
def convert_in_to_cm(feet,inches):
    total_inches = feet*12 + inches
    return round((total_inches * 2.54,2))

def convert_distance(distance):
    inches = distance*12
    yards = distance/3
    miles = distance/5280
    return (round(inches,2),round(yards,2),round(miles,2))

####get absolute filepath
##import os
##print(os.path.abspath('path_filename'))
##
####print sum of digits in integer
##value = int(input("Enter an integer: "))
##total = 0
##for digit in str(value):
##    total += int(digit)


####sort files by date
##import glob,os
##files = glob.glob.('.*txt')
##files.sort(key=os.path.getmtime)
##files = glob.glob('*.txt')
##print(files)
####get contents of a module
##print(dir(math))
##
####hash a word
##word = str(input("Please enter a word: "))
##word = list(word)
##word = '-'.join(word)
##word = word.strip('-')
##print(word[1:len(word)-1])
##
####get copyright info
##print(sys.copyright)

####return number of arguments
####return script file name and number of arguments
##print(sys.argv[0],len(sys.argv))
####print all modules that exist
##print(sys.builtin_module_names)
###Get recursion limit
##print(sys.getrecursionlimit())

##concatenate N strings
colors = ['red','blue','green']
colors = '-'.join(colors)

##test if all values are greater than certain target number
##or use .all() function
def compare_numbers(values,target):
    for value in values:
        if value < target:
            return "Not all numbers are greater than " + str(target)
    return "All numbers are greater than target!"

import os
##check if it's filename or directory
##os.path.isdir(path),os.path.isfile(path)

##print ascii characters
print(ord('a'))
print(ord('c'))
print(ord('x'))

import string
#print digits and special characte
print(string.digits)
print(string.punctuation)
#convert from byte to list
byte_words = b'123'
print(list(byte_words))
number = '123'
if number.isdigit():
    print('YES!')

import time
#print current time
print(time.ctime())

##get info and clear screen
##import os,system
##os.system('ls')
##os.system('clear')
##get hostname where routine is running!
import socket
print(socket.gethostname())

##os.path.basename() gets the filename from a path
##determine if number is positive, negative or zero
def is_positive(number):
    if number == 0:
        return "It's neither positive or negative"
    elif number > 0:
        return "It's positive"
    elif number < 0:
        return "It's negative"
##filters out and removes numbers from list that are divisible by 15
values = list(filter(lambda x : x % 15, [2,4,14,15,30,45,60]))
print(values)
import os
##os.getegid() gets effective group id
##os.geteuid() gets uer id
##os.getgid() gets group ID
##os.getgroups() gets suppelemtan group ids
##os.path.isfile(file) refers to a file when you encounter path name

##get file lists from current directory
##import glob
##file_list = glob.glob('*')
##print(file_list)

##remove first value from a list
values = list(range(0,31))
values.pop(0)
print(values)

##raise error if value is NOT a number
while True:
    try:
        value = int(input("Enter a value: "))
    except TypeError:
        print("WRONG!")
    else:
        print(value)
        break

##filter positive numbers from a list
values = [2,4,15,-1,2,3,-12]
positive = list(filter(lambda x : x > 0, values))
print(positive)

##computer product of list of integers without using for loop
numbers = list(range(1,6,1))
i,total = len(numbers) - 1,1
while i >= 0:
    total *= numbers[i]
    i -= 1
print(total)

from functools import reduce
##using lambdas to get product of numbers in list W/O loops
nums_product = reduce( (lambda x, y: x * y), numbers)
print(nums_product)


##see if 2 values having same ids have same memory location
def compare(s1,s2):
    if hex(id(s1)) == hex(id(s2)):
        return "Same!"
    else:
        return "Different!"
##create a bytearray from a list
values = list(range(1,16,1))
print(bytearray(values))

value = 213.45134235235
##display floating number to 2 digits
print('%.2f' %(value))
print('%f' %(value))
##format a number to 6
print('%.6f' %(value))

##program raises NameError if variable does not exist
try:
    value = 1
except NameError:
    print("DNE!")

##empty a variable WITHOUT destroying it
value = 19
print(type(value)())

##largest and smallest floats, ints and longs
import sys
print(sys.float_info)
print(sys.int_info)
print(sys.maxsize)
nums = [1,1,1,2,2,3,3,3,3]
##
##from collections import Counter
##total_counter = Counter(nums)
##numbers,frequency = list(total_counter.keys()), list(total_counter.values())
##for i in range(len(total_counter)):
##    total = numbers[i]*frequency[i]
##    print(total)
####checks if integer bit fits in 64 bits
####if int_val.bit_length() <= 63:
##
####uses any() function to print any lowercase letters
##string = 'ABCD34234234abdeefh'
##print(any(letter.islower() for letter in string))
####adds certain number of zeroes to the left of string!
##string.ljust(31,'0')
##print(string)
##
####print 2 integers on the same line
####x = int(input("Enter first value: "))
####y = int(input("Enter second value: "))
####print(x,y,end=' ')
####
##value = input('Enter a value: ')
##value = value.replace(' ','')
##
####convert 'True' to 1 and 'False' to 0
##x = True
##y = False
##print(int(x))
##print(int(y))
##
####convert decimal to hexadecimal
##print(format(30,'02x'))
##
##def sum_cube_integers(value):
##    if value <= 0:
##        return "Enter a positive integer"
##    total = 0
##    for i in range(value):
##        total += i ** 3
##    return total
##print(sum_cube_integers(3))
##
####get distinct pair of integers whose product is odd from sequence ofint
##values = list(range(1,11))
##start_value = values[0]
##for j in range(1,len(values)):
##    if (start_value*values[j]) % 2 == 1:
##        print (start_value,values[j])
##        break
##    
####Find max/min from sequence of numbers
##values_list = [4,8,84,321,23,43,53]
##start_value = values_list[0]
##for i in range(1,len(values_list)-1):
##    if start_value < values_list[i]:
##        start_value = values_list[i]
##print(start_value)    


##print every 3rd element from list until it's empty
##[1,2,3,4,5,6,7,8,9,10]
##[1,2,4,5,7,8,10]
##[1,2,5,7,10]
def remove_third_element(numbers):
    pos = 2
    index = 0
    len_list = len(numbers) - 1
    while len_list > 0:
        index = (pos + index) % (len_list)
        print(index)
        len_list -= 1
remove_third_element(list(range(1,11)))
