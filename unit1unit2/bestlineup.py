import sys

fin = open('lineup.in', 'r')
fout = open('lineup.out', 'w')
num_cases = int(fin.readline())

for j in range(num_cases):
    ints = int(fin.readline())
    int_arr = list(map(int, fin.readline().split(' ')))
    suffix_max = [(int_arr[-1], ints - 1)] * ints
    for i in range(len(suffix_max) - 2, -1, -1):
        if int_arr[i] > suffix_max[i + 1][0]:
            suffix_max[i] = (int_arr[i], i)
        else:
            suffix_max[i] = suffix_max[i + 1]
    for i in range(len(suffix_max)):
        if int_arr[i] != suffix_max[i][0]:
            int_arr.pop(suffix_max[i][1])
            int_arr.insert(i, suffix_max[i][0])
            break
    if j == 1:
        print(int_arr)
    stack = []
    for i in range(len(int_arr)):
        while stack and stack[-1] < int_arr[i]:
            stack.pop()
        stack.append(int_arr[i])
    for i in range(len(stack)):
        stack[i] = str(stack[i])
    fout.write(' '.join(stack))
    if j != num_cases - 1:
        fout.write('\n')