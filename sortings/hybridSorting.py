import random
from mergeSort import merge_sort
from insertionSort import insertion_sort            

def hybrid_sort(arr , THERSHOLD):
   merge_sort(arr , THERSHOLD) 

if __name__ == "__main__":
    SIZE = 50
    THRESHOLD = 6
    arr = [random.randint(1, 50) for _ in range(SIZE)]
    print("Original Array:", arr)
    hybrid_sort(arr, THRESHOLD)
    print("Sorted Array:", arr)

