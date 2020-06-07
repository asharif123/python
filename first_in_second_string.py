##iterate thru each letter in s1
##use .find to find first letter in s2
##return true if all s1 letters are in s2 in order!!
##

def first_in_second_string(s1,s2):
    index = s2.find(s1[0])
    for letter in s1:
        index = s2.find(letter,index)
        if index == -1:
            return ("NO!")
    return "YES!"
print(first_in_second_string('donor','Nabucodonosor'))
print(first_in_second_string('donut','Nabucodonosor'))
print(first_in_second_string('bcns','Nabucodonosor'))
print(first_in_second_string('bcsn','Nabucodonosor'))
        

##def first_in_second_string(s1,s2):
##    s1,s2 = s1.lower(),s2.lower()
####use the first s1 letter found in s2 as starting instance to find...
####subsequent letters
##    first_index = s2.find(s1[0])
##    if first_index == -1:
##        return "No"
####search for indices from s1 in s2 starting from second letter in s1
####.find() returns -1 if no indices are found
####if -1, it means not all letters of s1 in that order are found in s2.
##    for i in range(1,len(s1)):
##        first_index = s2.find(s1[i],first_index)
##        if first_index == -1:
##            return "No"
##    return "Yes"

##print(first_in_second_string('donor','Nabucodonosor'))
##print(first_in_second_string('donut','Nabucodonosor'))
##print(first_in_second_string('bcsn','Nabucodonosor'))
