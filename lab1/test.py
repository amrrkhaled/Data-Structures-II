import time
import random
import matplotlib.pyplot as plt
from bubbleSort import bubble_sort
from selectionSort import selection_sort
from insertionSort import insertion_sort

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def measure_execution_time(sort_function, arr):
    arr_copy = arr[:]  
    start_time = time.perf_counter()
    sort_function(arr_copy)
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000  # Convert to milliseconds

def main():
    sizes = [100, 200, 500, 1000, 5000, 10000, 25000]  
    bubble_times = []
    selection_times = []
    insertion_times=[]

    for size in sizes:
        arr = generate_random_array(size)  
        bubble_time = measure_execution_time(bubble_sort, arr)
        selection_time = measure_execution_time(selection_sort, arr)
        insertion_time=measure_execution_time(insertion_sort,arr)

        bubble_times.append(bubble_time)
        selection_times.append(selection_time)
        insertion_times.append(insertion_time)

        print(f"Array Size: {size:<6} Bubble Sort Time: {bubble_time:<10.3f} ms, Selection Sort Time: {selection_time:<10.3f} ms, Insertion Sort Time: {insertion_time:<10.3f} ms")

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, bubble_times, marker='o', linestyle='-', label="Bubble Sort", color='r')
    plt.plot(sizes, selection_times, marker='s', linestyle='-', label="Selection Sort", color='b')
    plt.plot(sizes, insertion_times, marker='x', linestyle='-', label="Insertion Sort", color='#FFD700')

    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (ms)")
    plt.title("Bubble Sort vs Selection Sort vs Insertion Sort Execution Time (ms)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
