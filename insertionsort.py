py_arr = [3,61,4124,43,2312,33,2,14,5,6]

def insertion_sort(x):


    for i in range(1,len(x)):
        current = x[i]
        # print('Turn['+str(i)+']')
        # print('Current is ' + str(current))
        # print('++++++++++++++++++++')
        while i > 0 and current < x[i-1]:
            # print('Position is ' + str(i))
            # print(x[i-1])
            # print(x)
            x[i] = x[i-1]
            i -= 1
            # print('to')
            # print(x)
            # print('-------------------')
        x[i] = current
        # print('After While')
        # print(x)
        # print('<><><><><><><><><><>')
    print('Sorted Array - ' + str(x))




insertion_sort(py_arr)