#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise ValueError('value of i is too large')
            else:
                res += (a ** b) / i
        except ValueError:
            res = b + a
            break
    return (res)
