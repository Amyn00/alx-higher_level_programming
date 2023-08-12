#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = ()
    lenght = len(sentence)
    first = sentence[0]
    if lenght == 0:
        my_tuple = 0, "None"
    else:
        my_tuple = lenght, first
    return (my_tuple)
