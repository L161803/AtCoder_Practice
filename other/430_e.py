T = int(input())
ans = []
for _ in range(T):
    A = input()
    B = input()
    if len(A) != len(B):
        ans.append("-1")
        continue
    n = len(A)
    pos = (A + A).find(B)
    ans.append(str(pos if 0 <= pos < n else -1))
print("\n".join(ans))