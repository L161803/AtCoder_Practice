import sys
sys.setrecursionlimit(10**7)

Directions = [
    (-1,-1),(-1,0),(-1,1),
    (0,-1),(0,1),
    (1,-1),(1,0),(1,1)
]

def dfs(r, c):
    Grid[r][c] = "."

    for dr, dc in Directions:
        nr = r + dr
        nc = c + dc

        if((0<=nr<N)and(0<=nc<M) and 
           (Grid[nr][nc] == "w")):
            
            dfs(nr, nc)
            

N, M = map(int, input().split())
Grid = [list(input()) for _ in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        if Grid[i][j] == "w":
            dfs(i, j)
            count += 1

print(f"LakeCount : {count}")
