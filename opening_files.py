import os

from math import pi
os.chdir("C:\Users\Awad\Desktop")
#print os.getcwd() + '\n'

##reading files from current directory!
##with keyword closes the file automatically once no longer needed!

##with open('Monthly_Expenses_to_Renew.txt') as document:
####    info = document.read()
####    print info
##
###read each letter one at a time!
####    for line in info:
####        print line
##
###reads each line one at a time!
###readline splits each line as a list!
##    read_file = document.readlines()
####   # print read_file
##    for line in read_file:
##        print line.rstrip()

##with open('learning_python.txt') as document:
##    read_info = document.readlines()
##    num = 0
##
##    for line in read_info:
##        print line

##
##write contents in a file named "practice_file.txt"
##filename = "practice_file.txt"
##with open(filename,'w') as file_open:
##    file_open.write("I am learning how to write in a file!\n")
##    file_open.write("Hi there!\n")

####use 'a' (append) mode if you want to write more content without overwriting anything!
##with open(filename,'a') as document:
##    document.write("Today is Thursday, March 14 2019\n")
##    document.write("You should have all of your content\n")
##
##with open(filename) as read_file:
##    read = read_file.readlines()
##    for line in read:
##        print line

while True:
    guest_name = str(raw_input("PLease enter your name: "))

    guests_list = "guests.txt"
    with open(guests_list,'w') as document:
        document.write((guest_name))

    with open(guests_list) as read_document:
        read = read_document.readlines()
        for line in read:
            print line

##guests = "guests_book.txt"
##while True:
##    guest_names = raw_input("Please enter your name: ")
##    guest_names = guest_names + "\n"
##    with open(guests,'w') as write_file:
##        write_file.write(guests)
        

    




