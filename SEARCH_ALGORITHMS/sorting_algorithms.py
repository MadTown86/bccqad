#!/usr/bin/env python3
"""
Comprehensive Sorting Algorithms Implementation Guide
==================================================

This document implements the most prevalent sorting algorithms with examples,
time/space complexity analysis, and practical usage notes.
"""

import random
import time
from typing import List, Any


def bubble_sort(arr: List[Any]) -> List[Any]:
    """
    Bubble Sort - O(n²) time, O(1) space
    
    Simple comparison-based algorithm that repeatedly steps through the list,
    compares adjacent elements and swaps them if they're in wrong order.
    """
    arr = arr.copy()  # Don't modify original
    n = len(arr)
    
    for i in range(n):
        # Flag to optimize - if no swaps occur, array is sorted
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    
    return arr


def selection_sort(arr: List[Any]) -> List[Any]:
    """
    Selection Sort - O(n²) time, O(1) space
    
    Finds the minimum element and places it at the beginning,
    then repeats for the remaining unsorted portion.
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        # Find minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum with first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


def insertion_sort(arr: List[Any]) -> List[Any]:
    """
    Insertion Sort - O(n²) time, O(1) space
    
    Builds the sorted array one item at a time by inserting each element
    into its correct position among the previously sorted elements.
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


def merge_sort(arr: List[Any]) -> List[Any]:
    """
    Merge Sort - O(n log n) time, O(n) space
    
    Divide-and-conquer algorithm that divides array into halves,
    recursively sorts them, then merges the sorted halves.
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer (merge)
    return merge(left, right)


def merge(left: List[Any], right: List[Any]) -> List[Any]:
    """Helper function to merge two sorted arrays"""
    result = []
    i = j = 0
    
    # Merge elements in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def quick_sort(arr: List[Any]) -> List[Any]:
    """
    Quick Sort - O(n log n) average, O(n²) worst case time, O(log n) space
    
    Divide-and-conquer algorithm that picks a pivot element and partitions
    the array around it, then recursively sorts the partitions.
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def heap_sort(arr: List[Any]) -> List[Any]:
    """
    Heap Sort - O(n log n) time, O(1) space
    
    Uses a binary heap data structure to sort. Builds a max heap,
    then repeatedly extracts the maximum element.
    """
    arr = arr.copy()
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
        heapify(arr, i, 0)  # Call heapify on reduced heap
    
    return arr


def heapify(arr: List[Any], n: int, i: int):
    """Helper function to maintain heap property"""
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def counting_sort(arr: List[int]) -> List[int]:
    """
    Counting Sort - O(n + k) time, O(k) space where k is range of input
    
    Non-comparison based algorithm that counts occurrences of each element.
    Only works with non-negative integers with known range.
    """
    if not arr:
        return arr
    
    # Find the range of the input
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    # Create count array and initialize with zeros
    count = [0] * range_val
    output = [0] * len(arr)
    
    # Store count of each element
    for num in arr:
        count[num - min_val] += 1
    
    # Modify count array to store actual positions
    for i in range(1, range_val):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    return output


def radix_sort(arr: List[int]) -> List[int]:
    """
    Radix Sort - O(d × (n + k)) time, O(n + k) space
    where d is number of digits, k is range of digits
    
    Non-comparison based algorithm that sorts by individual digits,
    starting from least significant digit.
    """
    if not arr:
        return arr
    
    # Handle negative numbers by finding minimum
    min_val = min(arr)
    if min_val < 0:
        # Shift all numbers to make them non-negative
        shifted_arr = [x - min_val for x in arr]
        sorted_shifted = radix_sort_positive(shifted_arr)
        return [x + min_val for x in sorted_shifted]
    else:
        return radix_sort_positive(arr)


def radix_sort_positive(arr: List[int]) -> List[int]:
    """Helper function for radix sort with non-negative integers"""
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        arr = counting_sort_for_radix(arr, exp)
        exp *= 10
    
    return arr


def counting_sort_for_radix(arr: List[int], exp: int) -> List[int]:
    """Modified counting sort for radix sort"""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Store count of occurrences of digits
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
    
    # Change count[i] to actual position of digit in output
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    return output


def bucket_sort(arr: List[float], num_buckets: int = None) -> List[float]:
    """
    Bucket Sort - O(n + k) average time, O(n²) worst case, O(n + k) space
    
    Distributes elements into buckets, sorts individual buckets,
    then concatenates. Works well for uniformly distributed data.
    """
    if not arr:
        return arr
    
    if num_buckets is None:
        num_buckets = len(arr)
    
    # Find range
    min_val, max_val = min(arr), max(arr)
    if min_val == max_val:
        return arr
    
    # Create buckets
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute elements into buckets
    for num in arr:
        # Calculate bucket index
        bucket_index = int((num - min_val) / (max_val - min_val) * (num_buckets - 1))
        buckets[bucket_index].append(num)
    
    # Sort individual buckets and concatenate
    result = []
    for bucket in buckets:
        if bucket:
            result.extend(insertion_sort(bucket))  # Use insertion sort for small buckets
    
    return result


def shell_sort(arr: List[Any]) -> List[Any]:
    """
    Shell Sort - O(n log n) to O(n²) time depending on gap sequence, O(1) space
    
    Generalization of insertion sort that allows exchange of items
    that are far apart, gradually reducing the gap between compared elements.
    """
    arr = arr.copy()
    n = len(arr)
    
    # Start with a big gap, then reduce it
    gap = n // 2
    
    while gap > 0:
        # Perform insertion sort for elements at gap distance
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # Shift earlier gap-sorted elements up until correct location found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
        
        gap //= 2
    
    return arr


def benchmark_algorithms():
    """
    Benchmark different sorting algorithms with various input sizes and types
    """
    print("Sorting Algorithms Benchmark")
    print("=" * 50)
    
    # Test data sets
    datasets = {
        "Small Random": [random.randint(1, 100) for _ in range(20)],
        "Medium Random": [random.randint(1, 1000) for _ in range(100)],
        "Nearly Sorted": list(range(100)) + [random.randint(1, 100) for _ in range(10)],
        "Reverse Sorted": list(range(100, 0, -1)),
        "All Same": [42] * 50
    }
    
    # Algorithms to test (excluding those with specific requirements)
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort),
        ("Shell Sort", shell_sort)
    ]
    
    for dataset_name, data in datasets.items():
        print(f"\nDataset: {dataset_name} ({len(data)} elements)")
        print("-" * 40)
        
        for algo_name, algo_func in algorithms:
            try:
                start_time = time.time()
                result = algo_func(data)
                end_time = time.time()
                
                # Verify sorting correctness
                is_sorted = all(result[i] <= result[i + 1] for i in range(len(result) - 1))
                status = "✓" if is_sorted else "✗"
                
                print(f"{algo_name:15}: {end_time - start_time:.6f}s {status}")
                
            except Exception as e:
                print(f"{algo_name:15}: Error - {e}")


def demonstrate_algorithms():
    """
    Demonstrate each sorting algorithm with simple examples
    """
    print("Sorting Algorithms Demonstration")
    print("=" * 50)
    
    # Sample data
    sample_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {sample_data}")
    print()
    
    # Demonstrate each algorithm
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort),
        ("Shell Sort", shell_sort)
    ]
    
    for name, func in algorithms:
        result = func(sample_data)
        print(f"{name:15}: {result}")
    
    # Special cases for algorithms with specific requirements
    print(f"{'Counting Sort':15}: {counting_sort(sample_data)}")
    print(f"{'Radix Sort':15}: {radix_sort(sample_data)}")
    
    # Bucket sort with floats
    float_data = [0.64, 0.34, 0.25, 0.12, 0.22, 0.11, 0.90]
    print(f"{'Bucket Sort':15}: {bucket_sort(float_data)}")


if __name__ == "__main__":
    # Run demonstrations
    demonstrate_algorithms()
    print("\n" + "=" * 50 + "\n")
    
    # Run benchmarks (comment out for large datasets to avoid long execution)
    benchmark_algorithms()
    
    print("""
Algorithm Selection Guide:
========================

• Bubble Sort: Educational purposes only - very inefficient
• Selection Sort: Simple but inefficient - use for tiny datasets
• Insertion Sort: Good for small or nearly sorted datasets
• Merge Sort: Stable, consistent O(n log n) - good general choice
• Quick Sort: Fast average case but unstable worst case
• Heap Sort: Consistent O(n log n), in-place, but not stable
• Counting Sort: Excellent for integers with small range
• Radix Sort: Good for integers, can handle large numbers
• Bucket Sort: Excellent for uniformly distributed floating-point data
• Shell Sort: Better than insertion sort, good for medium-sized datasets

For most general purposes, use Merge Sort or Quick Sort.
For specific data types or constraints, consider the specialized algorithms.
""")