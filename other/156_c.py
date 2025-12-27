N = int(input())
X = list(map(int, input().split()))
# P = sum(X)//N -> これは問題がある
P = int((sum(X)/N)+0.5) # sum()は重い
ans = 0
for i in range(N):
    ans += (X[i]-P)**2
print(ans)