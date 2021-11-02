array = [11, 15, 25, 77, 27, 45, 30, 1, 9, 3, 7, 11]


def unique_arr(arr):
    new_list = []
    for i in arr:
        if i in new_list:
            print(i)
            return False
        else:
            new_list.append(i)
    return True

print(unique_arr(array))