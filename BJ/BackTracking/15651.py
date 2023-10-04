from itertools import product as pr
n, m = map(int, input().split())
print('\n'.join(map(' '.join, pr(map(str, range(1, n+1)), repeat=m))))
