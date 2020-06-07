##tuple basics, cannot replace or add items!
##to change items in tuple, you need to reasssign it!
values = (1,2,3)
values = (0,1,2,3)
print(values[0:])

buffet = ("salmon", "mashed potatoes", "french fries", "grits", "prime ribs")
#buffet[0] = "rice"
for items in buffet:
    print (items + '\n')

buffet = ("salmon", "mashed potatoes", "chips", "grits", "steak")
for items in buffet:
    print (items + '\n')

