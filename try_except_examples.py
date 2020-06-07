###Exception examples
##try:
##    print(5/0)
##except Exception as result:
##    print (result)
##
##try:
##    int("H")
##except Exception as error:
##    print(error)

##def printExcTree(main_class):
##    print(main_class.__name__)
####call the class recursively to print each subclass that falls under main_class
####use __subclasses__ feature to print out each individual subclass!
##    for subclass in main_class.__subclasses__():
##        printExcTree(subclass)
###printExcTree(Exception)

##def printargs(args):
##    lng = len(args)
##    if lng == 0:
##        print("EMPTY!")
##    elif lng == 1:
##        print ('ONE')
##    else:
##        print ('ALOT OF STUFF')
####
####raising the printargs() function in 3 diff ways
####first when no arguments are passed
##try:
##	raise Exception()
##except Exception as e:
###	print(e, e.__str__(), sep=' : ', end=' : ')
##	printargs(e.args)
##
##try:
##	raise Exception(["my exception"])
##except Exception as secondary:
###	print(e, e.__str__(), sep=' : ', end=' : ')
##	printargs(secondary.args)
##
##try:
##	raise Exception("mea", "taking","shower","random","spontaneous")
##except Exception as e:
###	print(e, e.__str__(), sep=' : ', end=' : ')
##	printargs(e.args)
##
##Build your own 'Exception' structure in a class when you want to create a large 'Class' structure in your class having arguments not in common with familiar things
##Ex: model activities of large pizza restaurant using hierarchy of exceptions

#this is a general 'Exception' structure containing 'pizza' and 'message' describing the problem
class PizzaError(Exception):
    def __init__(self,pizza,message):
##'message' argument is passed to superclass constructor 'Exception'
        Exception.__init__(self,message)
        self.pizza = pizza

##more descriptive method descibing 'too much cheese' needs a more descriptive method
class TooMuchCheeseError(PizzaError):
    def __init__(self,pizza,cheese,message=''):
        PizzaError.__init__(self,pizza,message)
        self.cheese = cheese

##function defines conditions for when errors are raised
def makePizza(pizza,cheese):
    if pizza not in ['margherita','capric','calzone']:
        raise PizzaError(pizza,'Ingredient not there')
    elif cheese > 100:
        raise TooMuchCheeseError(pizza,cheese,'Too much cheese')
    else:
        print ("Pizza Ready!")
#test out the 3 ingredients and cheese amounts on the raised errors!
for (pz,ch) in [('calzone',0),('margherita',110),('mafia',20)]:
    try:
        makePizza(pz,ch)
    except TooMuchCheeseError as tmce:
        print(tmce, tmce.cheese, sep=' ')
    except PizzaError as pe:
        print(pe, pe.pizza, sep=' ')


