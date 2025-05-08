# 📘 Data Structures and Algorithms

This repository contains Python implementations of core data structures and algorithms as part of an academic assignment. It includes sorting algorithms (O(n^2) and O(n log n)), Red-Black Tree with dictionary application, and graph algorithms including Topological Sort and Prim's Minimum Spanning Tree. Performance analysis is included for sorting algorithms.

---

## 📁 Folder Structure

```
DataStructures-and-Algorithms/
├── README.md
├── Sorting/
│   ├── bubble_sort.py
│   ├── selection_sort.py
│   ├── insertion_sort.py
│   ├── quick_sort.py
│   ├── merge_sort.py
│   ├── heap_sort.py
│   └── sort_analysis.py
├── RedBlackTree/
│   ├── red_black_tree.py
│   ├── dictionary_app.py
│   └── dictionary.txt
└── Graphs/
    ├── topological_sort.py
    ├── prims_algorithm.py
    └── sample_graph.txt

```

---

## ➖ Sorting Algorithms

Implemented sorting techniques:

### O(n^2) Algorithms:

* Bubble Sort
* Selection Sort
* Insertion Sort

### O(n log n) Algorithms:

* Quick Sort (Randomized pivot)
* Merge Sort
* Heap Sort

### ⌚ Performance Analysis:

* Random arrays generated for sizes: 1,000, 25,000, 50,000, 100,000
* Each algorithm is tested on identical copies of the array
* Execution time is printed and plotted (Time vs Array Size)
* Use of `time` module for precise measurement

> Output Example:

```
Running time for Bubble Sort is ... ms
Running time for Quick Sort is ... ms
```

### 📈 Graphs

* Time (ms) vs Array Size for all algorithms
* Created using Excel based on measured timings

---

## 🌳 Red-Black Tree

### Features:

* Insert
* Search
* Print Tree Height
* Print Black Height
* Print Tree Size

### Application: English Dictionary

* Load words from `dictionary.txt`
* Insert new word (if not duplicate)
* Lookup word (print YES/NO)

---

## 📚 Graph Algorithms

### 1. Topological Sort

* Implemented for Directed Acyclic Graphs (DAG)
* Produces valid topological ordering

### 2. Prim's Minimum Spanning Tree

* Input: Connected weighted undirected graph
* Output: MST using Prim's algorithm
* Visualization recommended: [Prim Visualization](https://www.cs.usfca.edu/~galles/visualization/Prim.html)

---

