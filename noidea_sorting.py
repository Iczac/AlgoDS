py_arr = [3,61,4124,43,2312,33,2,14,5,6]

def insertionsort(x):
    x = x

    i = 1
    swapped = False
    while i < len(x):
        current = x[i]

        if current < x[i-1]:
            print(x)
            x[i] = x[i-1]
            x[i-1] = current
            i+=1
            swapped = True
            print('to')
            print(x)
            print('----------')
        else:
            i+=1

    if swapped:
        insertionsort(x)
    else:
        print('Sorted Array')
        print(x)

insertionsort(py_arr)