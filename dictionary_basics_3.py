##dictionary 3
#Create a dream_vacation dictionary where you ask user for name and where his dream vacation is!
##
##dream_vacation = {}
##
##
##while True:
##
##    name = str(input("Please enter your name: "))
##    vacation = str(input("Please enter your ideal vacation place: "))
##    dream_vacation[name] = vacation
##    repeat = input("DO you want to add more vacation or names? Y or N: ").upper()
##    if repeat == "N":
##        break
##
##for name, vacation in dream_vacation.items():
##    print "\n%s wants to go to %s." %(name.title(), vacation.title())
##
##print dream_vacation
##print dream_vacation.items()

new_menu = []
menu = ['chicken tikka', 'chicken masala', 'biryani', 'haleem', 'naan', 'salad', 'naan', 'naan', 'gajar halwa']
#Used to remove more than one 'naan' entry!
while 'naan' in menu:
    menu.remove('naan')
print (menu)
while menu:
    old_menu = menu.pop()
    new_menu.append(old_menu)
print (sorted(new_menu,reverse=True))

from collections import OrderedDict
glossary = {}
#Use 'Ordereddict' to print out entries in order they were first entered
glossary = OrderedDict()
glossary['protect'] = 'keep safe'
glossary['female'] = 'girl'
glossary['tomato'] = 'fruit'
glossary['realistic'] = 'genuine'
print (glossary.items())
##for key, pair in glossary.items():
##    print key, pair
