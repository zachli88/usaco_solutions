"""
ID: lizach71
LANG: PYTHON3
TASK: prefix
"""

fin = open('prefix.in', 'r')
fout = open('prefix.out', 'w')

tokens = []
line = fin.readline()
while line != '.\n':
    tokens += line.split()
    line = fin.readline()
sequence = ''
line = fin.readline()
while line != '':
    sequence += line[:-1]
    line = fin.readline()
dp = [0] * (len(sequence) + 1)
for i in range(len(dp) - 2, -1, -1):
    for token in tokens:
        if i + len(token) < len(dp) and sequence[i:i + len(token)] == token:
            dp[i] = max(dp[i], len(token) + dp[i + len(token)])
fout.write(str(dp[0]) + '\n')