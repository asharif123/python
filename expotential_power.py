#power(2,3) = 2*power(2,2)
#power(2,2) = 2*power(2,1)
#power(2,1) = 2*power(2,0)
##power(2,3) = 2*2*2*power(2,0) = 2*2*2*1 = 8
def power(x,y):
    if y == 0 or (x == 0):
        return(1)
    else:
        return (x*power(x,y-1))
