"""
ID: lizach71
LANG: PYTHON3
TASK: runround
"""

fin = open('runround.in', 'r')
fout = open('runround.out', 'w')
import sys
M = int(fin.readline())

def runround(num):
    num = str(num)
    seen_digits = set([0])
    for i in range(len(num)):
        if num[i] in seen_digits:
            return False
    seen_digits = set()
    index = 0
    for _ in range(len(num)):
        digit = int(num[index])
        index = (index + digit) % len(num)
        if num[index] in seen_digits:
            return False
        seen_digits.add(num[index])
    return index == 0
num = M + 1
while True:
    if runround(num):
        fout.write(str(num) + '\n')
        sys.exit()
    num += 1