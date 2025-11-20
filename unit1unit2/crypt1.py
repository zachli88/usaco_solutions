"""
ID: lizach71
LANG: PYTHON3
TASK: crypt1
"""

fin = open('crypt1.in', 'r')
fout = open('crypt1.out', 'w')

N = int(fin.readline())
nums = list(map(int, fin.readline().split()))
num_set = set(nums)
count = 0
for a in nums:
    for b in nums:
        for c in nums:
            for d in nums:
                for e in nums:
                    f = a * 100 + b * 10 + c
                    g = d * 10 + e
                    h = f * e
                    i = f * d
                    if h >= 1000 or i >= 1000:
                        continue
                    valid = True
                    while valid and h > 0:
                        digit = h % 10
                        if digit not in num_set:
                            valid = False
                        h //= 10
                    while valid and i > 0:
                        digit = i % 10
                        if digit not in num_set:
                            valid = False
                        i //= 10
                    j = f * g
                    while valid and j > 0:
                        digit = j % 10
                        if digit not in num_set:
                            valid = False
                        j //= 10
                    if valid:
                        count += 1
fout.write(str(count) + '\n')