N, M = map(int, input().split())
A = list(map(int, input().split()))

tmp = sum(A)-M

if tmp in A:
    print("Yes")
else:
    print("No")