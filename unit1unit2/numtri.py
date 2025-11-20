"""
ID: lizach71
LANG: PYTHON3
TASK: numtri
"""

fin = open('numtri.in', 'r')
fout = open('numtri.out', 'w')

R = int(fin.readline())
rows = []
for _ in range(R):
    rows.append(list(map(int, fin.readline().split())))
dp = [[0] * R for _ in range(R)]
for r in range(R - 1, -1, -1):
    for c in range(r + 1):
        dp[r][c] = rows[r][c]
        if r != R - 1:
            dp[r][c] += max(dp[r + 1][c], dp[r + 1][c + 1])
fout.write(str(dp[0][0]) + '\n')