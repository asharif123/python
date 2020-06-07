import os

#Print the current directory
os.chdir("C:/Users/ashar/OneDrive/Documents/")
print(os.getcwd())      

#### Open files ####
### Open file, read or write it
## If writing, write content to the file
## Open the written file for reading
myfile = open("My Thoughts.txt")

##Read files ##
myfile = open("My Thoughts.txt", "r").readlines()
print(myfile.read())


###Read each line in a file
###print(myfile.readlines())
##
#########Write files##########
##document = open("My Thoughts.txt", "w")
##document.write("Hello My name is Awad")
##
##document = open("My Thoughts.txt", "r")
##print(document.read())
