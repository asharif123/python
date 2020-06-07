#####Read out the number of characters in a document
#####User inputs a character and program calculates number of times it appears

for x in range(3):
    row = (('-')*3 + '\n')*3
print (row)


##import os
##
##os.chdir('C:\Users\Awad\Documents')
##print(os.getcwd())
##
##filename = open("all_letters.txt", "r")
####print(type(filename))
####print filename
####total = 0
##
##search_letter = (input('Enter a single character: \n')).lower()
##total = 0
##count = 0
##for letter in filename.read():
##    total = total + 1
####    print letter
##    if letter == search_letter:
##        count = count + 1
####print count
##
##total_percentage = (round(((float(count))/total * 100), 3)) 
##print ("The number of times '%s' character appears in the all_letters.txt file is %s. \n") %(search_letter, count)
##print ("The total percentage is %s percent.") %(total_percentage)
#########Get all files with .txt in current directory
########for file in glob.glob("*.txt"):
########    print(file)
######
######def count_char(char):
######
######    total = 0
######    count = 0
######
######
######    
######
######    #.read() = Reads every single character in the file
######    for letter in filename.read():
######        total = total + 1
######
###### #Reads number of times character inputted by user exists in file!
######        if char == letter:
######            count = count + 1
######
#######Prints the number of times letter inputted by user appears in the file!
######    #print(count)
######
#######Prints the total number of characters in the file
######    print("The number of times the letter %s appears in file is %s times.") %(char,count)
######
#######Print the total percentage letter occupies file and rounds to 3 digits .
######    percentage = round((float(count)/(total)) * 100, 3)
######    print("{0} - {1}%".format(char, percentage))
######    
######    
##
