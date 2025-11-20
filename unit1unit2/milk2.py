"""
ID: lizach71
LANG: PYTHON3
TASK: milk2
"""

fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')

num_intervals = int(fin.readline())
intervals = []
for _ in range(num_intervals):
    start, end = map(int, fin.readline().split())
    intervals.append([start, end])
intervals.sort()
head, tail = intervals[0][0], intervals[0][1]
max_overlap = tail - head
max_pause = 0
for i in range(1, len(intervals)):
    interval = intervals[i]
    if interval[0] > tail:
        max_pause = max(max_pause, interval[0] - tail)
        head, tail = interval[0], interval[1]
    else:
        tail = max(tail, interval[1])
    max_overlap = max(max_overlap, tail - head)
fout.write(str(max_overlap) + ' ' + str(max_pause) + '\n')