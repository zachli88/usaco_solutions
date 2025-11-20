"""
ID: lizach71
LANG: PYTHON3
TASK: transform
"""
import sys

def rotate(board):
    l, r = 0, len(board) - 1
    while l < r:
        for i in range(r - l):
            top_left = board[l][l + i]
            board[l][l + i] = board[r - i][l]
            board[r - i][l] = board[r][r - i]
            board[r][r - i] = board[l + i][r]
            board[l + i][r] = top_left
        l, r = l + 1, r - 1

def reflect(board):
    for i in range(len(board)):
        for j in range(len(board) // 2):
            board[i][j], board[i][len(board) - j - 1] = board[i][len(board) - j - 1], board[i][j]
            
fin = open('transform.in', 'r')
fout = open('transform.out', 'w')

N = int(fin.readline())
original = []
transformed = []
for _ in range(N):
    line = fin.readline()
    row = []
    for c in line[:-1]:
        row.append(c)
    original.append(row)
for _ in range(N):
    line = fin.readline()
    row = []
    for c in line[:-1]:
        row.append(c)
    transformed.append(row)
for i in range(1, 4):
    rotate(original)
    if original == transformed:
        fout.write(str(i) + '\n')
        sys.exit()
rotate(original)
reflect(original)
if original == transformed:
    fout.write(str(4) + '\n')
    sys.exit()
for _ in range(4):
    rotate(original)
    if original == transformed:
        fout.write(str(5) + '\n')
        sys.exit()
reflect(original)
if original == transformed:
    fout.write(str(6) + '\n')
    sys.exit()
fout.write(str(7) + '\n')

