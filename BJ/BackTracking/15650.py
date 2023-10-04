from itertools import combinations as cb
N, M = map(int, input().split())
print('\n'.join(' '.join(i) for i in cb(map(str, range(1, N+1)), M)))