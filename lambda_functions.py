##an anonymous function is a function without a name. In Python, anonymous functions are created with the lambda keyword. These functions are used for various purposes:

##they are handy in situations where we only need to use the function once
##they are lightweight when we need to break down complex tasks into small, specific tasks
##they are convenient as arguments to functions that require functions as parameters

my_list = ['test_string',99,lambda x : x ** 2]
print(my_list[2](5))

add10 = lambda x : x + 10
print(add10(12))

##map() function
value = [1,2,3,4,5]
values = list(map(lambda x : x ** 2, value))
##filter out values that are divisible by 2!
filtered_values = list(filter(lambda x : x % 2, value))
print(filtered_values)
print(values)
