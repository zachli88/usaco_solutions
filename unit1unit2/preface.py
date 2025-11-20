"""
ID: lizach71
LANG: PYTHON3
TASK: preface
"""

fin = open('preface.in', 'r')
fout = open('preface.out', 'w')

N = int(fin.readline())
symbols = [['I', 'V'], ['X', 'L'], ['C', 'D'], ['M']]
dp = {'I':0, 'V':0, 'X':0, 'L':0, 'C':0, 'D':0, 'M':0}
for num in range(1, N + 1):
    counts = {'I':0, 'V':0, 'X':0, 'L':0, 'C':0, 'D':0, 'M':0}
    for exponent in range(3, -1, -1):
        if num >= 9*10**exponent:
            num -= 9*10**exponent
            counts[symbols[exponent + 1][0]] += 1
            counts[symbols[exponent][0]] += 1
        if num >= 5*10**exponent:
            num -= 5*10**exponent
            counts[symbols[exponent][1]] += 1
        if num >= 4*10**exponent:
            num -= 4*10**exponent
            counts[symbols[exponent][1]] += 1
            counts[symbols[exponent][0]] += 1
        while num >= 10**exponent:
            num -= 10**exponent
            counts[symbols[exponent][0]] += 1
    for key in counts:
        dp[key] += counts[key]
res = []
keys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
for key in keys:
    res.append(dp[key])
while res[-1] == 0:
    res.pop()
for i in range(len(res)):
    fout.write(keys[i] + ' ' + str(res[i]) + '\n')        