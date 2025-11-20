"""
ID: lizach71
LANG: PYTHON3
TASK: sort3
"""

fin = open('sort3.in', 'r')
fout = open('sort3.out', 'w')

N = int(fin.readline())
counts = {1:0, 2:0, 3:0}
nums = []
for _ in range(N):
    num = int(fin.readline())
    counts[num] += 1
    nums.append(num)
counts2 = {}
for i in range(N):
    j = 0
    if i < counts[1]:
        j = 1
    elif i < counts[1] + counts[2]:
        j = 2
    else:
        j = 3
    key = (j, nums[i])
    counts2[key] = counts2.get(key, 0) + 1
res = 0
for key, rev_key in [[(1,2), (2, 1)], [(1,3), (3, 1)], [(2,3), (3, 2)]]:
    min_count = min(counts2.get(key, 0), counts2.get(rev_key, 0))
    if min_count != 0:
        counts2[key] -= min_count
        counts2[rev_key] -= min_count
        res += min_count
oop = 0
for key in [(1, 2), (1, 3), (2, 3), (2, 1), (3, 1), (3, 2)]:
    oop += counts2.get(key, 0)
res += oop // 3 * 2
fout.write(str(res) + '\n')