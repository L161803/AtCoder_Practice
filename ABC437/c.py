import sys
input = sys.stdin.readline

line = input().strip()
T = int(line)

for _ in range(T):
    
    line = input().strip()
    N = int(line)
    W = []
    P = []
    
    for _ in range(N):
        w, p = map(int, input().split())
        W.append(w)
        P.append(p)

    total_power = sum(P)
    cost = []

    for i in range(N):
        cost.append(W[i] + P[i])

    cost.sort()

    current = 0
    ans = 0

    for c in cost:
        if current + c <= total_power:
            current += c
            ans += 1
        else:
            break

    print(ans)