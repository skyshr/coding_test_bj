from itertools import permutations as pm, combinations as cb
N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
A, s = [], set()
for i in cb(a, M):
    if i not in s:
        s.add(i)
        for k in pm(i, M):
            A.append(k)
print('\n'.join(' '.join(map(str, i)) for i in sorted(set(A))))