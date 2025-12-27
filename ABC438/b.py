import sys
input = sys.stdin.readline

n, m = map(int, input().split())
S = input()
T = input()

min_total = float("inf")

for i in range(n-m+1):
    curr = 0
    for j in range(m):
        s_digit=int(S[i+j])
        t_digit=int(T[j])
        diff = (s_digit-t_digit+10)%10
        curr += diff

    if curr < min_total:
        min_total = curr

print(min_total)