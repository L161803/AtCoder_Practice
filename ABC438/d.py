import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

acc_B = [0]*(n+1)
for i in range(n):
    acc_B[i+1] = acc_B[i]+B[i]

suffix_C = [0]*(n+1)
for i in range(n-1,-1,-1):
    suffix_C[i] = suffix_C[i+1]+C[i]

acc_diff = [0]*(n+1)
for i in range(n):
    acc_diff[i+1] = acc_diff[i]+(A[i]-B[i])

ans = -float("inf")
curr_max = -float("inf")

for y in range(2,n):
    if acc_diff[y-1]>curr_max:
         curr_max=acc_diff[y-1]

    curr_score = acc_B[y]+suffix_C[y]+curr_max
    if curr_score>ans:
        ans = curr_score

print(ans)