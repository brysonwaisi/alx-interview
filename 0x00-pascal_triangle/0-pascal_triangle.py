#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    res = []
    if type(n) is not int or n <= 0:
        return res
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            elif i > 0 and j > 0:
                row.append(res[i - 1][j - 1] + res[i - 1][j])
        res.append(row)
    return res

# Time Complexity O(n^2)
# Space Complexity 0(n^2)