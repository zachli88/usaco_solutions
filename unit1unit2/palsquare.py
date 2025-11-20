"""
ID: lizach71
LANG: PYTHON3
TASK: palsquare
"""
import math

fin = open('palsquare.in', 'r')
fout = open('palsquare.out', 'w')
base = int(fin.readline().strip())

for i in range(1, 301):
    square = i * i
    num = []
    while square > 0:
        digit = square % base
        num.append(digit)
        square //= base
    palindrome = True
    l, r = 0, len(num) - 1
    while l < r:
        if num[l] != num[r]:
            palindrome = False
            break
        l, r = l + 1, r - 1
    if palindrome:
        for j, digit in enumerate(num):
            if digit >= 10:
                num[j] = chr((digit - 10) + ord('A'))
            else:
                num[j] = str(num[j])

        index = []
        while i > 0:
            digit = i % base
            index.append(digit)
            i //= base
        index.reverse()
        for j, digit in enumerate(index):
            if digit >= 10:
                index[j] = chr((digit - 10) + ord('A'))
            else:
                index[j] = str(index[j])
        fout.write(''.join(index) + " " + ''.join(num) + '\n')