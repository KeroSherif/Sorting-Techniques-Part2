import random
import time

def generate_random_array(size):
    return [random.randint(1, 100000) for _ in range(size)]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        insert_index = i
        current_value = arr[i]

        for j in range(i - 1, -1, -1):
            if arr[j] > current_value:
                arr[j + 1] = arr[j]
                insert_index = j
            else:
                break

        arr[insert_index] = current_value


if __name__ == "__main__":
    
    sizes = [30000, 2500, 5000]
    #sizes = [10000, 25000, 50000, 100000]

    for size in sizes:
        print(f"\nSorting an array of size {size}...")

        original_arr = generate_random_array(size)

        bubble_arr = original_arr.copy()
        selection_arr = original_arr.copy()
        insertion_arr = original_arr.copy()

        # Bubble Sort
        start_time = time.time()
        bubble_sort(bubble_arr)
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        print(f"Running time for Bubble Sort is {duration:.2f} ms")

        # Selection Sort
        start_time = time.time()
        selection_sort(selection_arr)
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        print(f"Running time for Selection Sort is {duration:.2f} ms")

        # Insertion Sort
        start_time = time.time()
        insertion_sort(insertion_arr)
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        print(f"Running time for Insertion Sort is {duration:.2f} ms")
        
       
        

   
        