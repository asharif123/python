##The yield statement suspends function’s execution and sends a value back to the caller,
##but retains enough state to enable function to resume where it is left off.
##When resumed, the function continues execution immediately after the last yield run.
##This allows its code to produce a series of values over time,
##rather than computing them at once and sending them back like a list, yield prints a series of values

###yield turns the function into a generator

##def print_values(n):
##    for i in range(n):
##        yield i
##
##for value in print_values(5):
##    print(value)
##

##def iter_values(n):
##    for i in range(n):
##        yield i*i
##
##
##for value in iter_values(13):
##    if value > 81:
##        break
##    print(value)

##def powers_of_2(number):
##    power = 1
##    for i in range(number):
##        yield power
##        power *= 2
##
##t = [value for value in powers_of_2(5)]
##print(t)
##
##for i in range(20):
##    if i in powers_of_2(4):
##        print(i)

##def Fib(n):
##    a,b = 1,1
##    i = 0
##    while i < n:
##        if i == 0:
##            yield 0
##        i += 1
##        if i == 1 or i == 2:
##            yield 1
##        else:
##            total = a + b
##            yield total
##            a,b = b,total
##        
##for value in Fib(10):
##    print(value)

##def factorial(number):
##    total = 1
##    for value in range(number+1):
##        if value == 0 or value == 1:
##            yield 1
##        else:
##            total *= value
##            yield total
##for value in factorial(5):
##    print(value)

def fibonacci(number):
    a,b = 1,1
    for value in range(0,number+1):
        if value == 0:
            yield 0
        elif value == 1 or value == 2:
            yield 1
        else:
            total = a + b
            yield total
            a,b = b,total

for value in fibonacci(11):
    print(value)
            
        
        
