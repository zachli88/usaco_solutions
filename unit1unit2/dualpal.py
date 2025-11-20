"""
ID: lizach71
LANG: PYTHON3
TASK: dualpal
"""
fin = open('dualpal.in', 'r')
fout = open('dualpal.out', 'w')
line = fin.readline().split(' ')
N, S = int(line[0]), int(line[1])
count = 0
curr = S + 1
while count < N:
    base_count = 0
    for base in range(2, 11):
        curr_num = curr
        num = []
        while curr_num > 0:
            digit = curr_num % base
            num.append(digit)
            curr_num //= base
        palindrome = True
        l, r = 0, len(num) - 1
        while l < r:
            if num[l] != num[r]:
                palindrome = False
                break
            l, r = l + 1, r - 1
        if palindrome:
            base_count += 1
        if base_count == 2:
            fout.write(str(curr) + '\n')
            count += 1
            break
    curr += 1
            