n, l, r = map(int, input().split())
s = list(input())
tmp = s[l-1:r]
print("Yes" if all(i=="o" for i in tmp) else "No")