def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def kth_smallest(arr,k):
    low = 0
    high = len(arr)-1
    while low <= high:
        pivot_index = partition(arr,low,high)
        if pivot_index == k-1:
            return arr[pivot_index]
        elif pivot_index > k-1:
            high = pivot_index - 1
        else:
            low = pivot_index + 1
    


arr = [3, 41,16, 25, 63, 52, 40]
k = 3
print(kth_smallest(arr, k))