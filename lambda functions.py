#Lambda Functions used to pass simple function as argument to another function
#Only requires single expression

double = ((lambda x:x*2))
print(double(7))

triple = lambda x: x*3
add = lambda x,y: x+y
print(add(triple(3),4))


#map function: takes function and iterable as arguments, returns new iterable

nums = [11,22,33,44,55]
result = map(lambda x: x+5, nums)
print(result)

##Filter filters out items that mismatch constraint
##Filter out numbers that are divisible by 2!
values = [11,22,33,44,55]
total = filter(lambda x: x % 2 == 0, values)
print(total)

i = 5
while True:
    print(i)
    i = i - 1
    if i < 0:
        break

