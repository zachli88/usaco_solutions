import sys

num_cases = int(sys.stdin.readline())

for j in range(num_cases):
    n = int(sys.stdin.readline())
    FjFavCows = list(map(int, sys.stdin.readline().split()))
    
    # Build suffix maximum array (each element is a tuple (value, index))
    suffix_max = [(FjFavCows[-1], n - 1)] * n
    for i in range(n - 2, -1, -1):
        if FjFavCows[i] > suffix_max[i + 1][0]:
            suffix_max[i] = (FjFavCows[i], i)
        else:
            suffix_max[i] = suffix_max[i + 1]
    
    # Perform the one allowed move if beneficial
    for i in range(n):
        if FjFavCows[i] != suffix_max[i][0]:
            FjFavCows.pop(suffix_max[i][1])
            FjFavCows.insert(i, suffix_max[i][0])
            break
    
    # Build lexicographically greatest subsequence using a monotonic stack
    stack = []
    for num in FjFavCows:
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
    
    print(' '.join(map(str, stack)))