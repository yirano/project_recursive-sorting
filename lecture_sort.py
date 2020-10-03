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
    if len(numbers) <= 1:
        return numbers

    left, pivot, right = partition(numbers)
    pivot = [pivot]

    sorted_array = quicksort(left) + pivot + quicksort(right)
    return sorted_array
