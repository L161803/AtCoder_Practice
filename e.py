import sys

sys.setrecursionlimit(10**6)

line1 = sys.stdin.readline()
N = int(line1)

line2 = sys.stdin.readline()
P = list(map(lambda x: int(x)-1, line2.split()))

visited = [False] * N
ans = 0

for i in range(N):
    if not visited[i]:
        count = 0
        curr = i

        while not visited(curr):
            visited[curr] = True
            curr = P[curr]
            count += 1

        ans += count*(count-1)//2

print(ans)