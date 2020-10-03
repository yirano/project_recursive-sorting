# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge_1(arrA, arrB, merged=[]):
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


def merge(arrA, arrB):
    return arrA + arrB


def merge_sort(arr):
    middle = len(arr)//2

    for i in arr[1:middle]:
        print(i)
        if arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
    for j in arr[middle+1:]:
        print(j)
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr


# TO-DO: implement the Merge Sort function below recursively
arr1 = [5, 3, 7, 2, 4, 1, 6, 8, 10, 9]

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
