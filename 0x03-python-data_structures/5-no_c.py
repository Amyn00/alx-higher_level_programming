#!/usr/bin/python3
def no_c(my_string):
    j = 0
    copy = my_string
    for i in range(len(my_string)):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            copy = copy[:(i - j)] + my_string[(i + 1):]
            j += 1
    return (copy)
