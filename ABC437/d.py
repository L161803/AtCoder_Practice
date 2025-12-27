import sys
import bisect

sys.setrecursionlimit(10**7)

input_data = sys.stdin.read().split()
    
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
B_cum = [0] * (M + 1)


for i in range(M):
    B_cum[i+1] = B_cum[i] + B[i]

MOD = 998244353
ans = 0

for a in A:

    idx = bisect.bisect_right(B, a)

    sum_bhalf_B = B_cum[idx]
    t1 = idx * a - sum_bhalf_B

    sum_ahalf_B = B_cum[M] - B_cum[idx]
    cnt_large = M - idx # aよりも大きいB[i]の数
    t2 = sum_ahalf_B - cnt_large * a

    ans += (t1+t2)%MOD

    print(ans)
