"""
ID: lizach71
LANG: PYTHON3
TASK: pprime
"""

fin = open('pprime.in', 'r')
fout = open('pprime.out', 'w')
import math
A, B = map(int, fin.readline().split())
def prime(num):
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
res = []
for a in range(10):
    num = a
    for b in range(10):
        num2 = num * 10 + b
        for c in range(10):
            num3 = num2 * 10 + c
            for d in range(10):
                num4 = num3 * 10 + d
                for e in range(11):
                    
                    rev_num = str(num4)[::-1]
                    if e != 10:
                        num5 = num4 * 10 + e
                    else:
                        num5 = num4
                    
                    # print(a, b, c, d, e, num5)
                    if rev_num != '0':
                        num5 = str(num5) + rev_num
                    num5 = int(num5)
                    if not (A <= num5 <= B):
                        continue
                    if prime(num5):
                        res.append(num5)
res.sort()
for num in res:
    fout.write(str(num) + '\n')