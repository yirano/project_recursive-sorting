def binary_search(arr, target, start, end):
    if len(arr) is 0:
        return -1
    middle_ind = (start + end) // 2
    if target == arr[middle_ind]:
        return middle_ind
    else:
        if target <= arr[middle_ind]:
            end = middle_ind - 1

        if target > arr[middle_ind]:
            start = middle_ind + 1

        return binary_search(arr, target, start, end)

    # STRETCH: implement an order-agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively


def agnostic_binary_search(arr, target):
    if len(arr) == 0:
        return -1
    start = 0
    end = len(arr) - 1
    middle = (start + end) // 2
    is_asc = start < end
    found = False

    if is_asc:
        while not found and end >= start:
            if arr[middle] == target:
                found = True
                return middle
            if arr[middle] > target:
                end = middle - 1
            if arr[middle] < target:
                start = middle + 1
            return agnostic_binary_search(arr, target)
        return -1
    else:
        while not found and end <= start:
            if arr[middle] == target:
                found = True
                return middle
            if arr[middle] > target:
                start = middle + 1
            if arr[middle] < target:
                end = middle - 1
            return agnostic_binary_search(arr, target)
        return -1
