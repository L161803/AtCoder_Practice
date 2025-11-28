#再帰回数の上限設定
import sys
sys.setrecursionlimit(10**7)


# 深さ優先探索の問題

Directions = [
    (-1,0),   # 上
    (1,0),    # 下
    (0,-1),   # 左
    (0,1),    # 右
]

visited = set()

def dfs(r:int, c:int, visited:set):
    if Grid[r][c] == "g": 
        return True
    
    visited.add((r,c))
    
    for (dr, dc) in Directions:
        nr = r + dr
        nc = c + dc

        if(((0<=nr<N) and (0<=nc<M))
           and (Grid[nr][nc] != "#")
           and (nr,nc) not in visited):
            if dfs(nr, nc, visited):
                return True


#入力
N, M = map(int, input().split())
Grid = [list(input()) for _ in range(N)]
idx_x, idx_y = -1, -1


# sを探す
for i in range(len(Grid)):
    for j in range(len(Grid[i])):
        if Grid[i][j] == "s": 
            idx_x = i
            idx_y = j
            break

flag = False
flag = dfs(idx_x, idx_y, visited)
if flag:
  print("Yes")
else:
  print("No")


