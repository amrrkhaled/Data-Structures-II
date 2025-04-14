def max_heapify(arr, i, heap_size):
    l = (2 * i) + 1  # Left child
    r = (2 * i) + 2  # Right child
    largest = i

    if l < heap_size and arr[l] > arr[largest]:
        largest = l
    if r < heap_size and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size)


def build_max_heap(arr):
    heap_size = len(arr)
    last_parent_index=heap_size // 2 - 1
    for i in range(last_parent_index, -1, -1):  # Start from the last parent
        max_heapify(arr, i, heap_size)


def heap_sort(arr):
    build_max_heap(arr)
    heap_size = len(arr)

    for i in range(len(arr) - 1, 0, -1): #start,stop,step

        arr[i], arr[0] = arr[0], arr[i]
        heap_size -= 1  # Reduce heap size
        max_heapify(arr, 0, heap_size)

        #len(arr)-1 start from last index of array
        #stop=0 stops before reaching 0
        #step=-1 loop runs in reverse order



