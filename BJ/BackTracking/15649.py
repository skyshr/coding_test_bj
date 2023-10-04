from itertools import permutations as pm
N, M = map(int, input().split())
L = [str(i) for i in range(1, N+1)]
answer = pm(L, M)
print('\n'.join(' '.join(i) for i in answer))