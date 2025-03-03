def sorter(arr):
    # For very small arrays, insertion sort could be faster
    if len(arr) < 10:
        insertion_sort(arr)
    else:
        # Using Python's built-in sort function which is based on Timsort.
        arr.sort()
    return arr
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
