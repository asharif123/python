##insertion sort
##iterate thru each value if value larger than previous ones:
##insert value to position where it would be smaller than preceding
##ex: 12,11,13,5,6
#i = 1, 11 less than 12 so insert 12 at index 1 and 11 before 12
#11,12,13,5,6
#i = 2, since 13 is larger than previous values, leave it alone
#i = 3, 5 is less than previous so shift 12,11,13 by 1 and move 5 to first position
#5,11,12,13,6
#i = 4, 6 is less than 11,12,13 and larger than first index so move 6 to second pos and
#shift 11,12,13 by index 1
# 5,6,11,12,13

def insertion_sort(arr):
    print("\nUnsorted array...")
    print(arr)
#start from second value because first value has no numbers before it to compare
    for i in range(1,len(arr)):
#compare each preceding value (ex: if starting at second index value, compare w/ first index value)
        for j in range(i-1,-1,-1):
#if value being tested (arr[i]) is less than arr[j], swap both
            if arr[i] < arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
#decrement by 1 to compare next set of values
#i will never be smaller than 0 because of the outer for loop we have defined
                i -= 1
                print(arr)
    print("\nFinal Output...")
    return(arr)
print(insertion_sort([9,3,78,12,76,0,-2]))
#print(insertion_sort([6,5,3,1,8,7,2,4,8,9]))
#print(insertion_sort([3,2,5,7,4]))

