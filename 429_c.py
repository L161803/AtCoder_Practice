import sys
from collections import Counter

N = int(input())
A = list(map(int, sys.stdin.buffer.read().split()))
ans = 0

m = Counter(A)
for k in m.keys():
    if m[k] >= 2:#m[k]で内の要素のうち値が2以上のものでループ
      ans += ((m[k]*(m[k]-1))//2) * (N-m[k])

print(ans)