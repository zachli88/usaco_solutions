"""
ID: lizach71
LANG: PYTHON3
TASK: gift1
"""
# from collections import defaultdict
fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

num_friends = int(fin.readline())
money_map = {}
friends = []
for _ in range(num_friends):
    name = fin.readline()
    money_map[name] = 0
    friends.append(name)

for _ in range(num_friends):
    curr = fin.readline()
    money, num_split = list(map(int, fin.readline().split()))
    if num_split == 0:
        continue
    money_map[curr] -= money // num_split * num_split
    for _ in range(num_split):
        friend = fin.readline()
        money_map[friend] += money // num_split

for name in friends:
    fout.write(name[:-1] + " " + str(money_map[name]) + '\n')