"""
ID: lizach71
LANG: PYTHON3
TASK: hamming
"""

fin = open('hamming.in', 'r')
fout = open('hamming.out', 'w')
N, B, D = map(int, fin.readline().split())
res = [0]
curr = 1
def dist(num1, num2):
    count = 0
    for _ in range(B):
        if num1 & 1 != num2 & 1:
            count += 1
        num1 >>= 1
        num2 >>= 1
    return count
while len(res) < N:
    valid = True
    for num in res:
        if dist(num, curr) < D:
            valid = False
            break
    if valid:
        res.append(curr)
    curr += 1
i = 0
while i < len(res):
    end = min(len(res), i + 10)
    num_set = res[i:end]
    fout.write(' '.join(map(str, num_set)) + '\n')
    i = end