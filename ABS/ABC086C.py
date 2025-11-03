# ABC086C - Traveling

N = int(input())
px = py = pt = 0  # 前の位置と時刻

for _ in range(N):
    t, x, y = map(int, input().split())
    dt = t - pt
    d = abs(x - px) + abs(y - py)
    if dt < d or (dt - d) % 2 != 0:
        print("No")
        break
    px, py, pt = x, y, t
    
else:
    print("Yes")