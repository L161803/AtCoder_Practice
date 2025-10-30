from collections import Counter
import sys

input = sys.stdin.readline
N = int(input().strip())
A = list(map(int, input().split()))
ans = 0

m = Counter(A)
s = sum(m.values())
for k in m.keys():
    if m[k]>1:#m[k]で内の要素のうち値が2以上のものでループ
      ans += ((m[k]*(m[k]-1))//2) * (N-m[k])

print(ans)