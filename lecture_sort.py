def partition(numbers):
    # this function breaks numbers into a left, pivot, and right
    left = []
    pivot = numbers[0]
    right = []

    # partition the numbers correctly into left and right arrays
    for num in numbers[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return left, pivot, right


def quicksort(numbers):
    # base case
    # what is the easiest array to sort?
    # "Conquer" step, it's just so easy
    if len(numbers) <= 1:
        return numbers

    # divide
    # figure out how to properly split our data
    left, pivot, right = partition(numbers)
    # make an array of size one with the pivot, this is now sorted
    pivot = [pivot]

    sorted_array = quicksort(left) + pivot + quicksort(right)
    return sorted_array
    # print(left)
    # print(pivot)
    # print(right)
