"""
ID: lizach71
LANG: PYTHON3
TASK: namenum
"""

def help(index):
    if index == len(num):
        res.append(''.join(curr))
        return
    digit = num[index]
    for c in num_to_letter[digit]:
        curr.append(c)
        help(index + 1)
        curr.pop()

name_set = set()
fin = open('namenum.in', 'r')
readnames = open('dict.txt', 'r')
fout = open('namenum.out', 'w')
num_to_letter = {'2':['A', 'B', 'C'], '3':['D', 'E', 'F'], '4':['G', 'H', 'I'], '5':['J', 'K', 'L'], '6':['M', 'N', 'O'], '7':['P', 'R', 'S'], '8':['T', 'U', 'V'], '9':['W', 'X', 'Y']}
line = readnames.readline()
while line:
    line = line.strip()
    name_set.add(line)
    line = readnames.readline()
num = fin.readline().strip()
res = []
curr = []
help(0)
count = 0
for name in res:
    if name in name_set:
        fout.write(name+'\n')
        count += 1
if count == 0:
    fout.write('NONE\n')