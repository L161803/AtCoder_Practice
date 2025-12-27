import sys
input = sys.stdin.readline

H, W, N = map(int, input().split())
line = []
cnt = [0] * H

for _ in range(H):
    line.append(list(map(int, input().split())))

for _ in range(N):
    b = int(input())

    for i in range(H):
        if b in line[i]:
            cnt[i] = cnt[i] + 1

print(max(cnt))