###reading contentes from a file
import os
os.chdir('C:/Users/Awad/Documents')
##with open('practice.txt') as read_file:
##    filename = read_file.readlines()
##    for line in filename:
##        print (line)

##count all letters in file
##total = 0
##with open('all_letters.txt') as filename:
##    read_file = filename.read()
##    for letter in read_file:
##        total = total + 1
##    print ("Total letters in file: " + str(total) + ".\n")
##
##total = 0
##with open('all_letters.txt') as filename:
##    for line in filename.readlines():
##        total = total + 1
##    print ('Total lines in file = ' + str(total))

#Replaec 'python' with 'C'
##with open('python_stuff.txt') as read_file:
##    read_file = read_file.readlines()
##    for line in read_file:
##        line = line.replace('Python','C')
##        print (line)

####write to a file!
##with open('new_file.txt','w') as filename:
##    contents = filename.write('Today is Saturday, August 17, 2019\n')
##    contents = filename.write('Time is 1:13 p.m.\n')
##    contents = filename.write('It is hot outside!\n')
##
##with open('python_stuff.txt') as read_file:
##    read_file = read_file.read()
##    print (read_file)


###use append mode to add content to existing file without overwriting
##with open('new_file.txt','a') as filename:
##    filename.write('I hate white supremacy\n')
##    filename.write('White supremacy has no place in USA\n')

##guest_list = []
##with open('guests.txt','w') as write_file:
##    while True:
##        guests = input('Please enter a guest name: ')
##        print ('Hello ' + guests + ', welcome to the party!\n')
##        guest_list.append(guests)
##        write_file.write(str(len(guest_list)) + ' - ' + guests + '\n')
##        #i = i + 1
##        if guests == 'x':
##            break
    
##with open('good_about_programming.txt','w') as write_file:
##    while True:
##        responses = input('Why do you like programming? ')
##        write_file.write('- ' + responses + '\n')
