"""
ID: lizach71
LANG: PYTHON3
TASK: ride
"""

import sys

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
word1 = fin.readline()
word2 = fin.readline()
mod1 = 1
for c in word1:
    mod1 = (mod1 * (ord(c) - ord('A') + 1)) % 47
mod2 = 1
for c in word2:
    mod2 = (mod2 * (ord(c) - ord('A') + 1)) % 47
if mod1 == mod2:
    fout.write("GO\n")
else:
    fout.write("STAY\n")