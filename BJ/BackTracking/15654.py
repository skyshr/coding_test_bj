from itertools import permutations as pm
N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

print('\n'.join(map(' '.join, pm([str(i) for i in a], M))))