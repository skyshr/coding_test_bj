from itertools import *
N, M = map(int,input().split())
for i in sorted(set(combinations(sorted(map(int, input().split())), M))):
    print(*i)