##prediction: invoke a() function and prints out 5
#1
def a():
    return 5
print(a())

##when a() is invoked, 5 is returned
##prediction: a() + a() equals 5 + 5 which equals 10
#2
def a():
    return 5
print(a()+a())

#3
#return returns one value or result and immmediately exits!
#herer we have 5 and 10 with 2 return statements
#prediction: when a() is invoked, 5 is printed
def a():
    return 5
    return 10
print(a())

#4
##here we have 5 being returned and 10 being printed
##My guess is that when a() is invoked, only 5 will be printed due to return 5 statement where return returns a value and exits immediately!
def a():
    return 5
    print(10)
print(a())

#5
#in a() function we print 5 so when invoked, 5 is immediately printed!
#we stored invoked function in x and when we print(x), None will also be printed due to no return statement and we're already printing 5
#prediction: 5 and None will be printed
def a():
    print(5)
x = a()
print(x)

###6
###we call a(b,c) twice
###a(1,2) = 1+2 = 3
###a(2,3) = 2+3 = 5
###print(a(1,2)+a(2,3)) = 3+5 = 8
###output is 8
##def a(b,c):
##    print(b+c)
##print(a(1,2) + a(2,3))

#7
#b is 2 and c is 5
#str(b) is '2' and str(c) is '5'
#we concatenate strings so answer is '25'
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#8
#b = 100
#prints 100
#since 100 is larger than 10, 10 is outputted
#in this case, None is NOT printed out since we have a return statement in the function!!
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())


#9
##a(2,3) outputs 7
##a(5,3) outputs 14
##a(2,3) + a(5,3) returns 21
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#10
##a(3,5) -> 3+5
##output is 8
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#11
##print(b) -> 500
##print(b) -> 500
##a() -> 300
##print(b) -> 500

b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#12
##print(b) -> 500
##print(b) -> 500
##a() -> 300 
##print(b) -> 500

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#13
##print(b) -> 500
##print(b) -> 500
##b=a() -> 300
##print(b) -> 300
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#14
#when a() is invoked, 1 is printed, then 3 then 2
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#15
##outputs 1,3,5
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
