"""
ID: lizach71
LANG: PYTHON3
TASK: castle
"""
from collections import deque

fin = open('castle.in', 'r')
fout = open('castle.out', 'w')

C, R = map(int, fin.readline().split())
rooms = [[0] * C for _ in range(R)]
floor_map = []

for _ in range(R):
    floor_map.append(list(map(int, fin.readline().split())))

def bfs(r, c, room_num):
    rooms[r][c] = room_num
    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        room_size[room_num] += 1
        can_pass = [True] * 4
        walls = floor_map[r][c]
        for i, num in enumerate([8, 4, 2, 1]):
            if walls >= num:
                walls -= num
                can_pass[i] = False
        for i, (dr, dc) in enumerate([[1, 0], [0, 1], [-1, 0], [0, -1]]):
            if not can_pass[i]:
                continue
            row, col = r + dr, c + dc
            if rooms[row][col] != 0:
                continue
            rooms[row][col] = room_num
            queue.append((row, col))
room_num = 1
room_size = {}
for r in range(R):
    for c in range(C):
        if rooms[r][c] == 0:
            room_size[room_num] = 0
            bfs(r, c, room_num)
            room_num += 1
max_room_combination = 0
remove_wall = None
directions = ['E', 'N']
for r in range(R):
    for c in range(C):
        for i, (dr, dc) in enumerate([[0, 1], [-1, 0]]):
            row, col = r + dr, c + dc
            if row < 0 or col < 0 or row == R or col == C:
                continue
            if rooms[row][col] == rooms[r][c]:
                continue
            combined_size = room_size[rooms[row][col]] + room_size[rooms[r][c]]
            if combined_size > max_room_combination:
                max_room_combination = combined_size
                remove_wall = (r, c, directions[i])
            elif combined_size == max_room_combination:
                if c > remove_wall[1]:
                    continue
                if c == remove_wall[1] and r < remove_wall[0]:
                    continue
                if r == remove_wall[0] and c == remove_wall[1] and remove_wall[2] == 'N':
                    continue
                remove_wall = (r, c, directions[i])
fout.write(str(room_num - 1) + '\n')
fout.write(str(max(room_size.values())) + '\n')
fout.write(str(max_room_combination) + '\n')
fout.write(str(remove_wall[0] + 1) + ' ' + str(remove_wall[1] + 1) + ' ' + remove_wall[2] + '\n')
