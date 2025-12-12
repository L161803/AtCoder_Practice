N, L, R = map(int, input().split())
S = list(input())

flag = True
for i in range(L-1,R):
    if S[i] == "x":
        flag = False

print("Yes" if flag else "No")