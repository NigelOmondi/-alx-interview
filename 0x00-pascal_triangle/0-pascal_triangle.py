#!/usr/bin/python3
"""
Pascal's triangle

"""


def pascal_triangle(n):
    """Return a list of lists of integers representing
    the Pascal’s triangle of n.
    Returns an empty list if n <= 0.
    Assume n will be always an integer
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    # Test the function with n = 5
    result = pascal_triangle(5)

    # Print the result
    for row in result:
        print(row)
