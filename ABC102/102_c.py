N = int(input())
A = list(map(int, input().split()))

B = [a-(i+1) for i, a in enumerate(A)]
B.sort()

medium = B[N//2]
ans = sum(abs(x-medium) for x in B)
print(ans)