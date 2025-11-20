"""
ID: lizach71
LANG: PYTHON3
TASK: lamps
"""

fin = open('lamps.in', 'r')
fout = open('lamps.out', 'w')

N = int(fin.readline())
C = int(fin.readline())
ON_LAMPS = set(list(map(int, fin.readline().split()))[:-1])
OFF_LAMPS = set(list(map(int, fin.readline().split()))[:-1])
lamps = [1] * (N + 1)
res = []
def dfs(index, c):
    global count
    if c > C:
        return
    if index == 4:
        for i in range(1, N + 1):
            if i in ON_LAMPS and lamps[i] == 0:
                return
            if i in OFF_LAMPS and lamps[i] == 1:
                return
        if (C - c) % 2 == 0:
            res.append(list(map(str, lamps.copy()[1:])))
        return
    dfs(index + 1, c)
    for i in range(1, N + 1):
        if index == 0:
            lamps[i] ^= 1
        if index == 1 and i % 2 == 1:
            lamps[i] ^= 1
        if index == 2 and i % 2 == 0:
            lamps[i] ^= 1
        if index == 3 and (i % 3) == 1:
            lamps[i] ^= 1
    dfs(index + 1, c + 1)
    for i in range(1, N + 1):
        if index == 0:
            lamps[i] ^= 1
        if index == 1 and i % 2 == 1:
            lamps[i] ^= 1
        if index == 2 and i % 2 == 0:
            lamps[i] ^= 1
        if index == 3 and (i % 3) == 1:
            lamps[i] ^= 1

dfs(0, 0)
if len(res) == 0:
    fout.write("IMPOSSIBLE\n")
else:
    # final = []
    # for seq in res:
    #     curr = ''
    #     for i in range(1, N + 1):
    #         curr += str(seq[i])
    #     final.append(curr)
    res.sort()
    for seq in res:
        fout.write(''.join(seq) + '\n')