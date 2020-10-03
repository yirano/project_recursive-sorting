# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    merged_arr = arrA + arrB

    if(merged_arr is not sorted(merged_arr)):
        merge_sort(merged_arr)

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    middle = len(arr) // 2
    left = []
    right = []
    for num in arr[:middle]:
        if num < arr[middle]:
            left.append(num)
        else:
            right.append(num)
    for num in arr[middle:]:
        if num < arr[middle]:
            left.append(num)
        else:
            right.append(num)

    return merge(left, right)


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr1))
# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
