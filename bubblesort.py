x = [64,23,112,4,5,7,3,2,8,43,42]

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


bubble_sort(x)

