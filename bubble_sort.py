def sorter(arr):
    n = len(arr)
    # Flag to optimize the algorithm by breaking early if no swaps occur
    has_swapped = True

    # Keep making passes through the array while swaps are still occurring
    while has_swapped:
        has_swapped = False
        # Loop through adjacent elements
        for i in range(n - 1):
            # Compare adjacent elements
            if arr[i] > arr[i + 1]:
                # Swap if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                has_swapped = True
        # Optimize by reducing the range since the largest element is now at the end
        n -= 1

    return arr
