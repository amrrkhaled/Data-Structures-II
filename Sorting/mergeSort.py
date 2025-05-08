import random
from insertionSort import insertion_sort

def merge_sort(arr):
   
        if(len(arr) > 1):
            mid = len(arr) // 2
            leftArray = arr[:mid]
            rightArray = arr[mid:]

            merge_sort(leftArray)
            merge_sort(rightArray)
            merge(leftArray , rightArray , arr)

def merge(leftArray , rightArray , arr):
    leftSize = len(arr) // 2
    rightSize = len(arr) - leftSize

    i = 0
    r = 0  
    l = 0       

    while l < leftSize and r < rightSize :
        if leftArray[l] < rightArray[r]:
            arr[i] = leftArray[l]
            l += 1
        else:
            arr[i] = rightArray[r]
            r += 1
        i += 1

    while l < leftSize:        
        arr[i] = leftArray[l]
        l += 1
        i += 1                                  

    while r < rightSize:
        arr[i] = rightArray[r]
        r += 1
        i += 1


