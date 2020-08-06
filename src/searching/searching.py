def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    first = 0
    end = len(arr) -1

    while first <= end:
        mid = first + ( end - first) // 2
        mid_value = arr[mid]
        if mid_value == target:
            return mid
        elif target < mid_value:
            end = mid -1
        else:
            first = mid + 1


    return -1  # not found
