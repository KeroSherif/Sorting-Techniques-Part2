from Sorting_Techniques_part1 import selection_sort


def hybrid_merge_sort(arr, threshold):

    # Check if the partition size is small enough to use Selection Sort
    if len(arr) <= threshold:
        return selection_sort(arr)  # Call your external selection_sort function

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
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Cleanup: Add any remaining elements from either list
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result