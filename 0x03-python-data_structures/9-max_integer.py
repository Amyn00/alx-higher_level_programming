#!/usr/bin/python3
def max_integer(my_list=[]):
    max_list = my_list[0]
    if len(my_list) == 0:
        return ("None")
    else:
        for i in range(len(my_list)):
            if max_list < my_list[i]:
                max_list = my_list[i]
    return (max_list)
