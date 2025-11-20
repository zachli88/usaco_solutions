"""
ID: lizach71
LANG: PYTHON3
TASK: skidesign
"""

fin = open('skidesign.in', 'r')
fout = open('skidesign.out', 'w')

N = int(fin.readline())
hills = []
for _ in range(N):
    hills.append(int(fin.readline()))

min_cost = float('inf')
for height in range(84):
    curr_cost = 0
    for hill in hills:
        if height <= hill <= height + 17:
            continue
        diff = min(abs(height - hill), abs(hill - (height + 17)))
        curr_cost += diff**2
    min_cost = min(min_cost, curr_cost)
fout.write(str(min_cost) + '\n')