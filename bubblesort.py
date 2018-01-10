py_arr = [3,61,4124,43,2312,33,2,14,5,6]

def bubble_sort(x):
    i = 0
    swapped = False
    while i < len(x)-1:
        first = x[i]
        second = x[i+1]
        if first < second:
            i += 1
        else:
            x[i] = second
            x[i+1] = first
            i += 1
            swapped = True

    if swapped:
        bubble_sort(x)
    else:
        print('Sorted Array - ' + str(x))


bubble_sort(py_arr)

