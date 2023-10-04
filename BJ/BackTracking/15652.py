from itertools import combinations_with_replacement as cwr
N, M = map(int, input().split())
print('\n'.join(map(' '.join, cwr(map(str, range(1, N+1)), M))))