def quicksort(array):
    sort(array, 0, len(array)-1)

def sort(array, first, last):
    if first < last:
        pivot = partition(array, first, last)
        sort(array, first, pivot - 1)
        sort(array, pivot + 1, last)

def partition(array, first, last):
    pivotvalue = array[first]
    left = first + 1
    right = last

    while True:
        while left <= right and array[left] <= pivotvalue:
            left += 1

        while array[right] >= pivotvalue and right >= left:
            right -= 1

        if right < left:
            break
        else:
            array[left], array[right] = array[right], array[left]

    array[first], array[right] = array[right], array[first]
    return right
