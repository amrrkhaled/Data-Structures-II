import random
from mergeSort import merge
from insertionSort import insertion_sort            

def merge_sort_hybrid(arr , THRESHOLD):
    if(len(arr) > THRESHOLD):
        if(len(arr) > 1):
            mid = len(arr) // 2
            leftArray = arr[:mid]
            rightArray = arr[mid:]

            merge_sort_hybrid(leftArray , THRESHOLD)
            merge_sort_hybrid(rightArray , THRESHOLD)
            merge(leftArray , rightArray , arr)
    else:
        insertion_sort(arr)


def hybrid_sort(arr , THERSHOLD):
    merge_sort_hybrid(arr , THERSHOLD) 

if __name__ == "__main__":
    SIZE = 50
    THRESHOLD = 6
    arr = [random.randint(1, 100) for _ in range(SIZE)]
    print("Original Array:", arr)
    hybrid_sort(arr, THRESHOLD)
    print("Sorted Array:", arr)

