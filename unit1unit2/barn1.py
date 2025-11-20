"""
ID: lizach71
LANG: PYTHON3
TASK: barn1
"""
import heapq

fin = open('barn1.in', 'r')
fout = open('barn1.out', 'w')

M, S, C = map(int, fin.readline().split())
occupied = []
for _ in range(C):
    occupied.append(int(fin.readline()))
occupied.sort()
gaps = []
last = occupied[0]
for i in range(1, len(occupied)):
    if occupied[i] != last + 1:
        gaps.append(occupied[i] - last - 1)
    last = occupied[i]
gaps.sort(reverse=True)
min_len = occupied[-1] - occupied[0] + 1
for i in range(min(M - 1, len(gaps))):
    min_len -= gaps[i]
fout.write(str(min_len) + '\n')