"""
ID: lizach71
LANG: PYTHON3
TASK: ariprog
"""

fin = open('ariprog.in', 'r')
fout = open('ariprog.out', 'w')

N = int(fin.readline())
M = int(fin.readline())

bisquares = set()
for p in range(M + 1):
    for q in range(M + 1):
        bisquares.add(p**2 + q**2)

def dfs(a, b, i):
    if i == N:
        return True
    if a not in bisquares:
        return False
    return dfs(a + b, b, i + 1)

count = 0
for b in range(1, 2 * M**2 // (N - 1) + 1):
    for a in range(2 * M**2 - (N - 1) * b + 1):
        if dfs(a, b, 0):
            count += 1
            fout.write(str(a) + ' ' + str(b) + '\n')

if count == 0:
    fout.write("NONE\n")