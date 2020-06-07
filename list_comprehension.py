##list comprehension
#syntax: [result, operation, range]
lst = []

for x in range(10):
    lst.append(1 if x % 2 == 0 else 0)

values = [1 if value % 2 == 0 else 0 for value in range(10)]
##Lambda functions are unidentifiable functions
##lambda is needed to declare as lambda function
#two is a parameterless function
##two = lambda z : 2
##sqr = lambda x : x * x
##power = lambda x,y = x ** y
##print(two)
##print(sqr(3))
##print(power(2,3))

##def printfunction(args, fun):
##    for x in args:
##        print('f(' + str(x) + ')' + ' = ' + str(fun(x)))
##
##def squared_values(x):
##    return x ** 2
##
##printfunction([x for x in range(0,11)], squared_values)
##print()
##
##def polynominal(number):
##    return number ** 2 + 2 * number - 1
##
##printfunction([number for number in range(-3,3)],polynominal)
##printfunction([number for number in range(3,3)], lambda number : number ** 2 + 2 * number - 1)

##map(function,list) takes a function and a list as arguments
##print(list(map(lambda x : x ** 2, [x for x in range(7)])))
list2 = list(map(lambda x : 2 ** x, [x for x in range(11)]))
for value in list2:
    print(value, end=' ')
print()
##filter(function,list of iterables)
##filters second argument using directions from first argument
import random
random_values = [random.randint(-10,10) for x in range(5)]
filtered_values = list(filter(lambda x : x % 2 and x > 0, random_values))
print(filtered_values)
def outer(par):
    loc = par
##inner() only invoked within outer()
    def inner():
        return loc
    return inner
##closure function
var = 1
fun = outer(var)
print(fun())
