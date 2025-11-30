import sys
input = sys.stdin.read

def solve():
    data = input().split()
    iterator = iter(data)
    try:
        N_str = next(iterator)
        N = int(N_str)
    except StopIteration:
        return

    MAX_SIZE = 2005
    grid = [[0] * MAX_SIZE for _ in range(MAX_SIZE)]
    clouds = []

    for _ in range(N):
        u, d, l, r = map(int, [next(iterator) for _ in range(4)])
        clouds.append((u, d, l, r))
        
        grid[u][l] += 1
        grid[u][r+1] -= 1
        grid[d+1][l] -= 1
        grid[d+1][r+1] += 1

    H_limit = 2002
    W_limit = 2002

    # 横方向
    for i in range(1, H_limit):
        for j in range(1, W_limit):
            grid[i][j] += grid[i][j-1]

    # 縦方向
    for j in range(1, W_limit):
        for i in range(1, H_limit):
            grid[i][j] += grid[i-1][j]
            
    empty = 0
    ones = [[0] * MAX_SIZE for _ in range(MAX_SIZE)]
    
    # 1~2000
    for i in range(1, 2001):
        for j in range(1, 2001):
            if grid[i][j] == 0:
                empty += 1
            elif grid[i][j] == 1:
                ones[i][j] = 1
    
    # 2次元累積和
    S = [[0] * MAX_SIZE for _ in range(MAX_SIZE)]
    for i in range(1, 2001):
        for j in range(1, 2001):
            S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + ones[i][j]
    
    for u, d, l, r in clouds:
        count = S[d][r] - S[u-1][r] - S[d][l-1] + S[u-1][l-1]
        print(empty + count)

solve()