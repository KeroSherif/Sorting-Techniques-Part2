import time
import random
from Sorting_Techniques_part1 import selection_sort,bubble_sort,insertion_sort

def generate_random_array(size):
    return [random.randint(1, 100000) for _ in range(size)]

def hybrid_merge_sort(arr, threshold):

    # Check if the partition size is small enough to use Selection Sort
    if len(arr) <= threshold:
        selection_sort(arr)  # Call your external selection_sort function
        return arr

    # Traditional Merge Sort: Divide the array into two halves
    mid = len(arr) // 2
    left_half = hybrid_merge_sort(arr[:mid], threshold)
    right_half = hybrid_merge_sort(arr[mid:], threshold)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):

    result = []
    i = j = 0

    # Compare elements and build the sorted result list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Cleanup: Add any remaining elements from either list
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)

def heap_sort(arr):
    
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_down(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_down(arr, i, 0)

    return arr
    
def heapify_down(arr,n,i):
    
    largest=i
    left=i*2+1
    right=i*2+2
    
    if left< n and arr[left]>arr[largest]:
        largest=left
    
    if right< n and arr[right]>arr[largest]:  
        largest=right 
    
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]    
        heapify_down(arr,n,largest)
        
if __name__ == "__main__":
    
    sizes = [30000, 2500, 5000]
    #sizes = [10000, 25000, 50000, 100000]

    for size in sizes:
        print(f"\nSorting an array of size {size}...")

        original_arr = generate_random_array(size)

        bubble_arr = original_arr.copy()
        selection_arr = original_arr.copy()
        insertion_arr = original_arr.copy()
        heap_arr=original_arr.copy()
        merge_arr=original_arr.copy()
        hybrid_merge_arr=original_arr.copy()
        quick_arr=original_arr.copy()

        # Bubble Sort
        start_time = time.time()
        #bubble_sort(bubble_arr)
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        print(f"Running time for Bubble Sort is {duration:.2f} ms")

        # Selection Sort
        start_time = time.time()
        #selection_sort(selection_arr)
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        print(f"Running time for Selection Sort is {duration:.2f} ms")

        # Insertion Sort
        start_time = time.time()
        #insertion_sort(insertion_arr)
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        print(f"Running time for Insertion Sort is {duration:.2f} ms")
        
        #Merge sort
        start_time = time.time()
        merge_sort(merge_arr)
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        print(f"Running time for merge Sort is {duration:.2f} ms")
        
        #Quick sort
        start_time = time.time()
        quicksort(quick_arr)
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        print(f"Running time for Quick Sort is {duration:.2f} ms")
        
        #heap sort
        start_time = time.time()
        heap_sort(heap_arr)
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        print(f"Running time for heap Sort is {duration:.2f} ms")
        
        #Hyprid Merge sort
        start_time = time.time()
        hybrid_sorted = hybrid_merge_sort(hybrid_merge_arr, threshold=32)
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        print(f"Running time for hyprid merge Sort is {duration:.2f} ms")
        