"""
ID: lizach71
LANG: PYTHON3
TASK: milk3
"""

fin = open('milk3.in', 'r')
fout = open('milk3.out', 'w')

A, B, C = map(int, fin.readline().split())
capacity = [A, B, C]
def dfs():
    if curr[0] == 0:
        res.append(curr[2])
    for i in range(3):
        for j in range(3):
            pour = min(curr[i], capacity[j] - curr[j])
            curr[i] -= pour
            curr[j] += pour
            next_state = tuple(curr)
            if next_state not in seen:
                seen.add(next_state)
                dfs()
            curr[i] += pour
            curr[j] -= pour
seen = set([(0, 0, C)])
curr = [0, 0, C]
res = []
dfs()
res.sort()
for num in res[:-1]:
    fout.write(str(num) + " ")
fout.write(str(res[-1]) + '\n')