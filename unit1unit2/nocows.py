"""
ID: lizach71
LANG: PYTHON3
TASK: nocows
"""

fin = open('nocows.in', 'r')
fout = open('nocows.out', 'w')

N, K = map(int, fin.readline().split())

dp = [[0] * (K + 1) for _ in range(N + 1)]
for c in range(K + 1):
    dp[0][c] = 1
for r in range(1, N + 1):
    if r % 2 == 0:
        continue
    for c in range(1, K + 1):
        for left in range(r):
            right = r - left - 1
            dp[r][c] = (dp[r][c] + dp[right][c - 1] * dp[left][c - 1]) % 9901
fout.write(str((dp[N][K] - dp[N][K - 1]) % 9901) + "\n")