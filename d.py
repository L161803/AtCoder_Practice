from collections import deque
import sys

sys.setrecursionlimit(10**6)

line1 = sys.stdin.readline().split()
H, W = map(int, line1)
grid = [sys.stdin.readline().strip() for _ in range(H)]
    

start = (0, 0)
goal = (H - 1, W - 1)

warp_points = {}
for r in range(H):
    for c in range(W):
        char = grid[r][c]
        if 'a' <= char <= 'z':
            if char not in warp_points:
                warp_points[char] = []
            warp_points[char].append((r, c))

dist = [[-1] * W for _ in range(H)]
dist[0][0] = 0
    
queue = deque([start])

used_warps = set()

drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while queue:
    r, c = queue.popleft()
    d = dist[r][c]

    if (r, c) == goal:
        print(d)
        exit()

    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != '#' and dist[nr][nc] == -1:
            dist[nr][nc] = d + 1
            queue.append((nr, nc))

    char = grid[r][c]
    if 'a' <= char <= 'z':
        if char not in used_warps:
            used_warps.add(char)
            for wr, wc in warp_points[char]:
                if dist[wr][wc] == -1:
                    dist[wr][wc] = d + 1
                    queue.append((wr, wc))

print(-1)