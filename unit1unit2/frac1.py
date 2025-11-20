"""
ID: lizach71
LANG: PYTHON3
TASK: frac1
"""

fin = open('frac1.in', 'r')
fout = open('frac1.out', 'w')
import heapq
heap = []
N = int(fin.readline())
seen = set()
for i in range(1, N + 1):
    for j in range(i + 1):
        if j/i not in seen:
            seen.add(j/i)
            heapq.heappush(heap, (j/i, str(j) + '/' + str(i)))
while heap:
    val, frac = heapq.heappop(heap)
    fout.write(frac + "\n")
