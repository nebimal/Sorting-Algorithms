import time
import random
import matplotlib.pyplot as plt

# CPU: Intel(R) Core(TM) i3-1000NG4 CPU @ 1.10GHz
# RAM: 8 GB 3733 MHz LPDDR4X
# System Version: macOS 15.2 (24C101)
# Kernel Version: Darwin 24.2.0

def InsertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
        
def SelectionSort(A):
    for i in range(len(A) - 1):
        min1 = i
        for j in range(i + 1, len(A)):
            if(A[j] < A[min1]):
                min1 = j
        A[i], A[min1] = A[min1], A[i]

def BubbleSort(A):
    for i in range (len(A) - 1):
        swapped = False
        for j in range (len(A) - 1, i, -1):
            if(A[j] < A[j-1]):
                A[j], A[j-1] = A[j-1], A[j]
                swapped = True
        if not swapped:
            break

def benchmark_sorting_algorithms():
    sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 5000, 10000, 25000]
    insertion_times = []
    selection_times = []
    bubble_times = []
    
    for n in sizes:
        A = random.sample(range(1, 30000), n)  
        
        start_time = time.time()
        InsertionSort(A.copy())
        insertion_times.append(time.time() - start_time)
        
        start_time = time.time()
        SelectionSort(A.copy())
        selection_times.append(time.time() - start_time)
        
        start_time = time.time()
        BubbleSort(A.copy())
        bubble_times.append(time.time() - start_time)
    
    plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
    plt.plot(sizes, selection_times, label='Selection Sort', marker='s')
    plt.plot(sizes, bubble_times, label='Bubble Sort', marker='^')
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Benchmarking Sorting Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()

benchmark_sorting_algorithms()
