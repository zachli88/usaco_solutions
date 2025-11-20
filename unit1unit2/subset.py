"""
ID: lizach71
LANG: PYTHON3
TASK: subset
"""

import sys
fin = open('subset.in', 'r')
fout = open('subset.out', 'w')

N = int(fin.readline())
target = int(N * (N + 1) / 2)
if target % 2:
    fout.write('0\n')
    sys.exit()
target //= 2
dp = [[0] * (target + 1) for _ in range(N + 2)]
for r in range(N + 2):
    dp[r][target] = 1
for r in range(N, 0, -1):
    for c in range(target - 1, -1, -1):
        dp[r][c] = dp[r + 1][c]
        if c + r <= target:
            dp[r][c] += dp[r + 1][r + c]

fout.write(str(dp[1][0] // 2) + '\n')