first = "James"
middle = "Michael"
last = "Buchanan"
full_name = ("%s %s %s")%(first, middle, last)
print (full_name.title())

print (full_name.upper())
print (full_name.lower())
print (full_name.title())
#Tabs the name to the right!
print("\t" + full_name)

famous_person = "Rene Descartes"
#print ("%s once said, \"A person who never made a mistake never tried anything new.\"") %(famous_person)
#.capitalize() only capitalizes first letter and NOT letters after letter
print (famous_person.capitalize())
#.title() titles the first letter and letters after first letter can be upper or lowercase!
print (famous_person.title())

#ord(): used to get the codepoint of each letter!

##center the string by adding certain amounts of space
##center inside field at certain width, width should be >= length of string
print('alpha'.center(5))
print('alpha'.center(20,'$'))

#.endswith() method returns True if condition is satisfied
#false if not satisfied
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

##.find() finds first occurence of string in word
#ex: t.find(parameter) finds the index of first occuring of parameter
#find(parameter,start,end), outputs -1 if no occurence!
print ('alpha'.find('c')) #outputs -1
print ('alpha'.find('a',2)) #outputs 4
print ('onomatopoeia'.find('o',1,len('onomatopoeia')-1)) #2

message = "  Hello world I am learning something! "
####print message
##
##message = " Hello world I am learning something! "
###strip white space on the right side
##print (message.rstrip())
##
###strip white space on left side
##print(message.lstrip())
##
#strip out right AND left white space using .strip()
print (message.strip())

###Using .title() capitalizes first letter of each word that comes after whitespace!
##print message.title()

###Capitalizes all letters ih message
##print message.upper()
wordlist = ['cat','dog','rabbit']
letterlist = []
for word in wordlist:
    for letter in word:
        letterlist.append(letter)
print (letterlist)

##.index() returns FIRST index occurence for character being searched!
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

##
###lower cases all letters
##print message.lower()
##msg = "Values {0} {1} {2} {3}".format("abra", "kadabra", "alakazam", "magic")
##print(msg)
##
######String functions
##
###joins edit, spam. and eggs to hello
print(" ".join(["edit", "spam", "eggs","gameboy"]))
##
###replace text
##sentence = "Hello man"
##print(sentence.replace("man", "world"))
##
##first_name = "Awad"
##last_name = "Sharif"
##
##print (first_name + " " + last_name)
##print "Hello Mr." + first_name.title () + " " + last_name.title()

#Split separates elements according to the delimiter provided
##
##print("spam", "carrots", "good", "bad", "ugly").split(",")
##
####a = min([sum([11,22])],max([abs(-30), 5**2]))
####print(a)
##print "Hello world!"
##message = "Hello world I am learning something!"
##print message

##if "epsilon".endswith("on"):
##    print("yes")
##else:
##    print("no")
##

# return -1 if index does not exist!
#1 if index exists
print("Eta".find("ta"))
print("Eta".find("mma"))

##find all indices of the word 'the'
txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)

#second argument says where to start finding the string
##print('kappa'.find('a', 2)) #4
##message = "Hello world I am learning something!"
###Using .title() capitalizes first letter of each word that comes after whitespace!
##print message.title()
##print "Asdfsdfadsgsgadsfasdfdsaf".title()
###Capitalizes all letters ih message
##print message.upper()
###lower cases all letters
##print message.lower()

#.isalnum(): returns True if string only contains either letters or numbers
#.isdigit(): returns True if string only contains digits
#.isspace9): returns True if string only contains whitespace
##ex: print('lambda_30'.isalnum()) returns false as '_' is NOT letter or #
#.isalpha(): returns True if string only contains letters
