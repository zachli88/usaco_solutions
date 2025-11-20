"""
ID: lizach71
LANG: PYTHON3
TASK: combo
"""

fin = open('combo.in', 'r')
fout = open('combo.out', 'w')

N = int(fin.readline())
combo1 = list(map(int, fin.readline().split()))
combo2 = list(map(int, fin.readline().split()))

valid = set()
for a in range(1, N + 1):
    option1 = True
    option2 = True
    if abs(combo1[0] - a) > 2 and (min(combo1[0], a) + N - max(combo1[0], a)) > 2:
        option1 = False
    if abs(combo2[0] - a) > 2 and (min(combo2[0], a) + N - max(combo2[0], a)) > 2:
        option2 = False
    if not option1 and not option2:
        continue
    for b in range(1, N + 1):
        option3 = option1
        option4 = option2
        if abs(combo1[1] - b) > 2 and (min(combo1[1], b) + N - max(combo1[1], b)) > 2:
            option3 = False
        if abs(combo2[1] - b) > 2 and (min(combo2[1], b) + N - max(combo2[1], b)) > 2:
            option4 = False
        if not option3 and not option4:
            continue
        for c in range(1, N + 1):
            option5 = option3
            option6 = option4
            if abs(combo1[2] - c) > 2 and (min(combo1[2], c) + N - max(combo1[2], c)) > 2:
                option5 = False
            if abs(combo2[2] - c) > 2 and (min(combo2[2], c) + N - max(combo2[2], c)) > 2:
                option6 = False
            if not option5 and not option6:
                continue
            valid.add((a, b, c))
fout.write(str(len(valid)) + '\n')
            