"""
ID: lizach71
LANG: PYTHON3
TASK: milk
"""
import heapq

fin = open('milk.in', 'r')
fout = open('milk.out', 'w')

N, M = map(int, fin.readline().split())
heap = []
for _ in range(M):
    P, A = map(int, fin.readline().split())
    heapq.heappush(heap, (P, A))

total_cost = 0
while N > 0:
    P, A = heapq.heappop(heap)
    amount = min(N, A)
    total_cost += amount * P
    N -= amount
fout.write(str(total_cost) + '\n')