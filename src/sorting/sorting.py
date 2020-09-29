# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB, merged=[]):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = merged
    curr = 0
    if len(arrA) == 0:
        merged_arr.append(arrB[0:])
        return merged_arr
    elif len(arrB) == 0:
        merged_arr.extend(arrA[0:])
        return merged_arr
    if arrA[curr] <= arrB[curr]:
        merged_arr.append(arrA[curr])
        return merge(arrA[curr+1:], arrB, merged_arr)
    else:
        merged_arr.append(arrB[curr])
        return merge(arrA, arrB[curr+1:], merged_arr)


# TO-DO: implement the Merge Sort function below recursively
arr1 = [3, 5, 6]
arr4 = [0, 1, 2, 3, 4, 5]

print(merge(arr1, arr4))


def merge_sort(arr):
    # Your code here
    return arr

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
