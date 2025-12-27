line = input().strip()
N = int(line)
grid = [[0] * N for _ in range(N)]
r = 0
c = (N - 1) // 2
grid[r][c] = 1
for k in range(1, N * N):
    val = k + 1
    nr = (r - 1) % N
    nc = (c + 1) % N
    if grid[nr][nc] == 0:
        r = nr
        c = nc
    else:
        r = (r + 1) % N
    grid[r][c] = val

for row in grid:
    print(*row)
