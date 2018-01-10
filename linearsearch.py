py_arr = [3,61,4124,43,2312,33,2,14,5,6]

#easier implementation with python built-in function
def linersearch_ezmode(data ,x):

    x = x
    data = data

    found = False

    for item in x:
        if data == item:
            found = True
            break
    if found:
        print("It exists")
    else:
        print("It doesn't exist")

#normal implementation
def linersearch(data, x):

    x = x
    data = data

    found = False

    i = 0

    while i < len(x):
        if data == x[i]:
            found = True
            break
        else:
            i += 1

    if found:
        print("It exists")
    else:
        print("It doesn't exist")


linersearch_ezmode(6,py_arr)

linersearch(3,py_arr)


