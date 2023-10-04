from itertools import combinations as cb
N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

print('\n'.join(map(' '.join, cb([str(i) for i in a], M))))