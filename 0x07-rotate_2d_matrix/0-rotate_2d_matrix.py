#!/usr/bin/python3
'''Rotate an nxn 2D matrix 90 deg clockwise'''
''' step 1 transpose matrix
step 2 reverse

Transpose ---> for i (0 -> len(a))
                    for j(i -> len(a))
                        a[i][j], a[j][i] = a[j][i], a[i][j]

Reversing ---> for i in range(n/2):
                    for j in range(n):
                        a[j][i], a[j][n-1-i] = a[j][n-1-i], a[j][i]'''


def rotate_2d_matrix(matrix):
    # transpose
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse
    n = len(matrix)
    for i in range(n//2):
        for j in range(n):
            matrix[j][i], matrix[j][n-1-i] = matrix[j][n-1-i], matrix[j][i]

    return matrix
# matrix = [[1,2,3,34], [4,5,6,77], [7,8,9,98]]
# print(rotate_2d_matrix(matrix))
# Time Complexity O(n^2) & Space Complexity O(1)
