from itertools import combinations_with_replacement as cwr
n, m = map(int, input().split())
arr = list(map(str, sorted(list(set(map(int, input().split()))))))
for i in cwr(arr, m):
    print(" ".join(i))