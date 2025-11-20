"""
ID: lizach71
LANG: PYTHON3
TASK: beads
"""

fin = open('beads.in', 'r')
fout = open('beads.out', 'w')

num_beads = fin.readline()
beads = fin.readline()[:-1]
beads = beads + beads
left_section = 0
curr = None
i = 0
right_w = 0
prev_w = 0
while i < len(beads) // 2:
    if beads[i] != 'w' and curr != None and curr != beads[i]:
        break
    if curr == None and beads[i] != 'w':
        curr = beads[i]
    if beads[i] == 'w':
        right_w += 1
    else:
        right_w = 0
    left_section += 1
    i += 1

max_necklace = 0
while i < len(beads) // 2:
    curr = beads[i]
    curr_section = 0
    left_section += prev_w
    prev_w = right_w
    right_w = 0
    while i < len(beads):
        # if i == 28:
        #     print(beads[i], beads[i] != 'w' and beads[i] != curr)
        if beads[i] != 'w' and beads[i] != curr:
            max_necklace = max(max_necklace, left_section + curr_section)
            # print(i, left_section, curr_section, max_necklace)
            left_section = curr_section
            curr_section = 0
            break
        if beads[i] == 'w':
            right_w += 1
        else:
            right_w = 0
        curr_section += 1
        i += 1

fout.write(str(max(max_necklace, left_section)) + '\n')
# w w w b b r w r b r b  r  r  b  r  b  r  w  r  w  w  r  b  w  r  w  r  r  b
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28