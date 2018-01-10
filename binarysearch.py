py_arr = [7,843,1,23,131]

def b_search(data,x):

    x = x
    data = data

    if len(x) != 0:
        first_half = round(len(x)/2)
        second_half = len(x) - first_half
        first_half_array = x[:first_half]
        second_half_array = x[second_half:]

        if x[first_half] != data and len(x) != 1:
            if x[first_half] < data:
                b_search(data,second_half_array)
            else:
                b_search(data,first_half_array)
        elif(x[first_half] == data):
            print('Found it')
        else:
            print('Not Found')
    else:
        print("It's an empty array")

b_search(131,py_arr)