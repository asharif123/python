##for loops basic I

##print all integers from 0 to 150
for i in range(151):
    print(i,)

##Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for j in range(5,1001,5):
    print(j)

##Print integers 1 to 100.
##If divisible by 5, print "Coding" instead.
##If divisible by 10, print "Coding Dojo".

for k in range(1,101):
    if (k % 5) == 0 and (k % 10) != 0:
        print("Coding")
    elif (k % 10) == 0:
        print("Dojo")
    else:
        print(k)

##Add odd integers from 0 to 500,000, and print the final sum.
total = 0
for l in range(500001):
    if (l % 2) != 0:
        total += l
print(total)

##Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
value = 2018
while value >= 0:
    print(value)
    value -= 4

##flexible counter
lowNum = 2
highNum = 29
mult = 5
for i in range(lowNum,highNum+1):
    if (i % mult) == 0:
        print(i)
