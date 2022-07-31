#!/usr/bin/python3
"""
task12
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    """
    if n <= 0:
        return []
    res = []
    l = []
    for x in range(n):
        row = []
        for y in range(x + 1):
            if x == 0 or y == 0 or x == y:
                row.append(1)
            else:
                row.append(l[y] + l[y - 1])
        l = row
        res.append(row)
    return 
