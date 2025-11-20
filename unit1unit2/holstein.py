"""
ID: lizach71
LANG: PYTHON3
TASK: holstein
"""

fin = open('holstein.in', 'r')
fout = open('holstein.out', 'w')

V = int(fin.readline())
vitamin_needs = list(map(int, fin.readline().split()))
G = int(fin.readline())
feed_vitamins = []
for _ in range(G):
    feed_vitamins.append(list(map(int, fin.readline().split())))

def dfs(i):
    valid = True
    for j in range(V):
        if curr_counts[j] < vitamin_needs[j]:
            valid = False
            break
    if valid:
        if len(res[0]) == 0 or len(res[0]) > len(curr_scoops):
            res[0] = curr_scoops.copy()
    if i == G:
        return
    for j, count in enumerate(feed_vitamins[i]):
        curr_counts[j] += count
    curr_scoops.append(i + 1)
    dfs(i + 1)
    for j, count in enumerate(feed_vitamins[i]):
        curr_counts[j] -= count
    curr_scoops.pop()
    dfs(i + 1)

curr_counts = [0] * V
curr_scoops = []
res = [[]]
dfs(0)
fout.write(str(len(res[0])))
for num in res[0]:
    fout.write(' ' + str(num))
fout.write('\n')