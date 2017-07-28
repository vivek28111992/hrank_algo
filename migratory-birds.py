#!/bin/python3

import sys


def migratoryBirds(n, ar):
    # Complete this function
    data = {}
    for i in range(n):
        key = ar[i]
        if key in data:
            data[key] += 1
        else:
            data[key] = 1
    res = max(data.keys(), key=(lambda k: data[k]))
    return res


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
