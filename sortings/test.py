import time
import random
import matplotlib.pyplot as plt
from bubbleSort import bubble_sort
from selectionSort import selection_sort
from insertionSort import insertion_sort
from quickSort import quick_sort_wrapper as quick_sort
from mergeSort import merge_sort_wrapper as merge_sort

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def measure_execution_time(sort_function, arr):
    arr_copy = arr[:]  
    start_time = time.perf_counter()
    sort_function(arr_copy)
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000  # Convert to milliseconds

def main():
    sizes = [100, 200, 500, 1000, 5000, 10000,25000]  
    bubble_times = []
    selection_times = []
    insertion_times=[]
    quick_sort_times=[]
    merge_times = []

    for size in sizes:
        arr = generate_random_array(size)  
        bubble_time = measure_execution_time(bubble_sort, arr)
        selection_time = measure_execution_time(selection_sort, arr)
        insertion_time=measure_execution_time(insertion_sort,arr)
        quick_sort_time=measure_execution_time(quick_sort,arr)
        bubble_times.append(bubble_time)
        selection_times.append(selection_time)
        insertion_times.append(insertion_time)
        quick_sort_times.append(quick_sort_time)
        merge_time = measure_execution_time(merge_sort, arr)
        merge_times.append(merge_time)

        print(f"\nArray Size: {size}")
        print(f"{'-'*70}")
        print(f"Bubble Sort     : {bubble_time:<7.3f} ms")
        print(f"Selection Sort  : {selection_time:<7.3f} ms")
        print(f"Insertion Sort  : {insertion_time:<7.3f} ms")
        print(f"Quick Sort      : {quick_sort_time:<7.3f} ms")
        print(f"Merge Sort      : {merge_time:<7.3f} ms")
        print(f"{'-'*70}")

    # Plot results
    plt.figure(figsize=(12, 6))

    # Logarithmic Scale
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, first plot
    plt.plot(sizes, bubble_times, marker='o', linestyle='-', label="Bubble Sort", color='r')
    plt.plot(sizes, selection_times, marker='s', linestyle='-', label="Selection Sort", color='b')
    plt.plot(sizes, insertion_times, marker='x', linestyle='-', label="Insertion Sort", color='#FFD700')
    plt.plot(sizes, quick_sort_times, marker='.', linestyle='-', label="Quick Sort", color='g')
    plt.plot(sizes, merge_times, marker='d', linestyle='-', label="Merge Sort", color='purple')

    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (ms) - Logarithmic Scale")
    plt.title("Sorting Algorithms - Logarithmic Scale")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # Logarithmic scale

    # Linear Scale
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, second plot
    plt.plot(sizes, bubble_times, marker='o', linestyle='-', label="Bubble Sort", color='r')
    plt.plot(sizes, selection_times, marker='s', linestyle='-', label="Selection Sort", color='b')
    plt.plot(sizes, insertion_times, marker='x', linestyle='-', label="Insertion Sort", color='#FFD700')
    plt.plot(sizes, quick_sort_times, marker='.', linestyle='-', label="Quick Sort", color='g')
    plt.plot(sizes, merge_times, marker='d', linestyle='-', label="Merge Sort", color='purple')

    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (ms) - Linear Scale")
    plt.title("Sorting Algorithms - Linear Scale")
    plt.legend()
    plt.grid(True)
    plt.gcf().canvas.manager.set_window_title("Sorting Algorithms Comparison")
    plt.tight_layout()  # Adjust spacing between subplots
    plt.show()

if __name__ == "__main__":
    main()
