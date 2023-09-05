#!/usr/bin/python3

"""
Write a function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    lines = text.split('.')
    for line in lines:
        if '?' in line:
            inter_line = line.split('?')
            for inter_line in inter_line:
                if ':' in inter_line:
                    two_point_line = inter_line.split(':')
                    for two_point_line in two_point_line:
                        two_point_line = two_point_line.strip()
                        if two_point_line:
                            print(two_point_line)
                    print("")
                else:
                    inter_line = inter_line.strip()
                    if inter_line:
                        print(inter_line)
            print("")
        else:
            line = line.strip()
            if line:
                print(line)
    print("")
