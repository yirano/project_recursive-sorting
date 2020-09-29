# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    print('>>>>>>>> start index: ', start)
    # print('>>>>>>>> middle index: ', middle_ind)
    print('>>>>>>>> end index: ', end)
    # print('>>>>>>>> value: ', arr[middle_ind])

    print('-----------------')
    found = False

    while end >= start and found is False:
        middle_ind = (start + end) // 2
        if target == arr[middle_ind]:
            found = True
            print('>>>>>>>> FOUND!!!: ', found)
            print('>>>>>>>> middle index: ', middle_ind)
            return middle_ind
        else:
            if target <= arr[middle_ind]:
                end = middle_ind - 1

            if target > arr[middle_ind]:
                start = middle_ind + 1

            return binary_search(arr, target, start, end)
    return -1

    # STRETCH: implement an order-agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass
