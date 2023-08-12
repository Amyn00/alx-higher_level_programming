#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n_tuple = ()
    t_a = tuple_a + (0, 0)
    t_b = tuple_b + (0, 0)
    n_tuple = t_a[0] + t_b[0], t_a[1] + t_b[1]
    return (n_tuple)
