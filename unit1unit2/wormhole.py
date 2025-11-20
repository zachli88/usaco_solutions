"""
ID: lizach71
LANG: PYTHON3
TASK: wormhole
"""

fin = open('wormhole.in', 'r')
fout = open('wormhole.out', 'w')

def check():
    for i in range(N):
        curr = i
        for _ in range(N):
            if next[curr] == None:
                break
            curr = pair[next[curr]]
        if next[curr] != None:
            return True
    return False

def dfs():
    global count
    i = 0
    while i < N and pair[i] != None:
        i += 1
    if i == N:
        if check():
            count += 1
            return
    for j in range(i + 1, N):
        if pair[j] == None:
            pair[i], pair[j] = j, i
            dfs()
            pair[i], pair[j] = None, None

N = int(fin.readline())
next = [None] * N
pair = [None] * N
wormholes = []
for _ in range(N):
    x, y = map(int, fin.readline().split())
    wormholes.append((x, y))

for i in range(N):
    for j in range(N):
        if wormholes[i][1] == wormholes[j][1] and wormholes[i][0] < wormholes[j][0]:
            if next[i] == None or wormholes[next[i]][0] > wormholes[j][0]:
                next[i] = j

count = 0
dfs()
fout.write(str(count) + '\n')