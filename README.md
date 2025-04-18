# 📚 Data Structures II

This repository contains Python implementations for several advanced data structures and algorithms covered in the **Data Structures 2** course. The code includes sorting algorithms, search optimizations, and the red-black tree data structure.

---

## 📌 Topics Covered

- 🧮 **Sorting Techniques**
  - Bubble Sort
  - Insertion Sort
  - Selection Sort
  - Merge Sort
  - Quick Sort (with randomized pivot)
  - Heap Sort
  - Hybrid Sort (Merge + Insertion)
  - Kth Smallest Element using Quickselect

- 🌳 **Red-Black Tree**
  - Red-Black Tree data structure
  - Black-height calculation
  - Basic insertion support and empty tree handling

- 📖 **Dictionary Search (Extra)**
  - Basic dictionary file loading and string lookup

---

## 📂 Repository Structure

```plaintext
📦 data-structures-2
│
├── 📜 README.md               # This file
├── 📂 sortings/               # Sorting algorithm implementations
│   ├── bubbleSort.py          # Bubble sort implementation
│   ├── heapSort.py            # Heap sort implementation
│   ├── hybridSorting.py       # Hybrid sort (Merge + Insertion)
│   ├── insertionSort.py       # Insertion sort implementation
│   ├── kth-Smallest.py        # Find kth smallest using Quickselect
│   ├── mergeSort.py           # Merge sort implementation
│   ├── quickSort.py           # Quick sort with randomized pivot
│   ├── selectionSort.py       # Selection sort implementation
│   └── test.py                # Test file for sorting algorithms
│
├── 📂 redBlackTree/           # Red-Black Tree implementation
│   ├── tree.py                # Main red-black tree implementation
│   ├── dictionary.py          # Loads dictionary and searches for words
│   └── Dictionary.txt         # Sample dictionary data
│
└── .gitignore                 # Standard gitignore file
