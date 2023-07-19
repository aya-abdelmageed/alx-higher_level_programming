#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """get a list of lists of integers representing the Pascal’s triangle"""
    ans = []
    if n == 0:
        return ans

    ans.append([1])
    for i in range(1, n):
        last = ans[-1]
        next = [1]

        for i in range(len(last) - 1):
            next.append(last[i] + last[i + 1])
        next += [1]
        ans. append(next)

    return ans
