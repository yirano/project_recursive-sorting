# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    i = 0
    j = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1

    return merged_arr + arrA[i:] + arrB[j:]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # divide the arrays
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    # merging sorted arrays
    return merge(left, right)


# arr1 = [2, 4, 9, 3, 7, 8]
# arr = [6, 2, 4, 8, 5, 1, 9, 7]
arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(merge_sort(arr))
# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):

    while start < mid and mid <= end:
        if arr[start] > arr[mid]:
            arr.insert(start, arr.pop(mid))
            start += 1
            mid += 1
        else:
            start += 1


def merge_sort_in_place(arr, left, right):
    if abs(left - right) > 1:

        middle = left + (right - left) // 2

        merge_sort_in_place(arr, left, middle)
        merge_sort_in_place(arr, middle + 1, right)
        merge_in_place(arr, left, middle + 1, right)
    else:
        merge_in_place(arr, left, right, right)


# print(arr)
# print(merge_sort_in_place(arr, 0, len(arr) - 1))
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort_in_place(arr1, 0, len(arr1)-1))
