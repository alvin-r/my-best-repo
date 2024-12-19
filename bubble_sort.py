def sorter(arr):

    # Start from the second element (index 1)
    for i in range(1, len(arr)):
        # Store the current element to be inserted
        key = arr[i]

        # Initialize j as the position before i
        j = i - 1

        # Move elements greater than key one position ahead
        # to make space for key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key in its correct position
        arr[j + 1] = key
    # i want a better sort
    return arr

def some_function_1():
    x = 1
    for i in range(100):
        print(i)
    for i in range(200):
        x += i
    return x

def some_function_2():
    x = 2
    for i in range(100):
        print(i)
    for i in range(200):
        x += i
    return x

def some_function_3():
    x = 3
    for i in range(100):
        print(i)
    for i in range(200):
        x += i
    return x