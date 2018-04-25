# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot

from datetime import datetime
startTime = datetime.now()


def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low , high):
 
        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
# Driver code to test above

from random import randrange
import numpy as np

arr=np.random.randint(100, size=100)
n = len(arr)

for i in range(n):
    print (str(arr[i]), end=' ')
    for j in range(arr[i]):
        print ("*", end=' ')
    print("")



quickSort(arr,0,n-1)

print("---------------------------------------------------")



for i in range(len(arr)):
    print (str(arr[i]), end=' ')
    for j in range(arr[i]):
        print ("*", end=' ')


    print("")


print(datetime.now() - startTime)

       
# This code is contributed by Mohit Kumra
