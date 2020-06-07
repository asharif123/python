#determines if number is prime or not

def is_prime(x):
##    x = int(x)
    if x <= 1:
        print "You cannot input anything less than 2\n!"
##    elif x == 2:
##        print "2 is a prime number\n!"
    elif x > 2:
        for n in range(2,x):
         
            if (x % n) == 0:
                print "%s is a composite number!\n" %(x)
                break
##            else:
##                print "It's a prime!"
##                break
##        return False
##x = int(raw_input("Please enter an integer greater than 2: "))
##
##for n in range(2,x):
##    if (x % n) == 0:
##        print x
##    
            
    
               
