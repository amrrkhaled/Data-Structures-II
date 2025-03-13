import random
from insertionSort import insertion_sort

def merge_sort(arr , THRESHOLD):
    if(len(arr) <= THRESHOLD):
        if(len(arr) > 1):
            mid = len(arr) // 2
            leftArray = arr[:mid]
            rightArray = arr[mid:]

            merge_sort(leftArray , THRESHOLD)
            merge_sort(rightArray , THRESHOLD)
            merge(leftArray , rightArray , arr)
    else:
        insertion_sort(arr)

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

def merge_sort_wrapper(arr):
    THRESHOLD = 0
    merge_sort(arr , THRESHOLD)

