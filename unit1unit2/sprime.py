"""
ID: lizach71
LANG: PYTHON3
TASK: sprime
"""

import math

fin = open('sprime.in', 'r')
fout = open('sprime.out', 'w')

N = int(fin.readline())
def dfs(curr, i):
    if i == N:
        fout.write(str(curr) + '\n')
        return
    for j in range(10):
        if i == 0 and j == 0:
            continue
        next = curr * 10 + j
        if prime(next):
            dfs(next, i + 1)
def prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
dfs(0, 0)