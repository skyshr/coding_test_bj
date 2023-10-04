from itertools import product as pr
N, M = map(int, input().split())
a = list(set(list(map(int, input().split()))))
a.sort()

print('\n'.join(map(' '.join, pr([str(i) for i in a], repeat=M))))