#!/usr/bin/python3
""" returns a list of lists of integers representing
the Pascal’s triangle of n"""


def pascal_triangle(n):
    """pascal triangle function
    Args:
        n (int): input
    Returns:
        List of lists of integer otherwise an empty list if n <= 0
    """
    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        triangle = triangles[-1]
        tmp = [1]
        for i in range(len(triangle) - 1):
            tmp.append(triangle[i] + triangle[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
