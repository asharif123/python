##selection sort

##iterate thru a list of numbers
##take each number, set it has minimum and compare with subsequent values
##if number is smaller than current min, set it as new min
##after traversing, min is smallest value and swap with first value in list
##first value will have minimum
##cont with subsequent values until all are swapped at correct pos and
##list is ordered

def selection_sort(arr):
    for i in range(len(arr)):
        min_value = i
        for j in range(i+1,len(arr)):
            if arr[min_value] > arr[j]:
                min_value = j
        arr[i],arr[min_value] = arr[min_value],arr[i]
    return arr
print(selection_sort([4,3,1,2,11]))
print(selection_sort([8,5,2,3,9,6,1,4,7]))
my_arr = [-64, 25, -12, 22, 11]
print(selection_sort(my_arr))
