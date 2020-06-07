##Bubble sort algorithm
##Iterate thru each pair of numbers at a time
##if the number preceding is bigger than adjacent, swap them
##Do this until the list has all numbers in order

##Ex: [5,4,6,3]
#[4,5,6,3],[4,5,6,3],[4,5,3,6]
#[4,5,3,6],[4,3,5,6],[4,3,5,6]
#[3,4,5,6],[3,4,5,6],[3,4,5,6]

def bubblesort(numbers_list):
    for k in range(len(numbers_list)):
#do a swap each time we traverse the array
        swap = 0
        for i in range(len(numbers_list)-1-k):
            if numbers_list[i] > numbers_list[i+1]:
                numbers_list[i],numbers_list[i+1] = numbers_list[i+1],numbers_list[i]
                swap += 1
                print(numbers_list)
#if no swap has occurred, we know the list is already in order
        if swap == 0:
            break
    print("\nArray after swapping...\n")
    return numbers_list
#print(bubblesort([5,4,6,3]))
print(bubblesort([6,5,3,1,8,7,2,4,21,14,11]))
#print(bubblesort([14,46,43,27,57,41,45,21,70]))
#print(bubblesort([64,34,25,12,22,11,90]))
