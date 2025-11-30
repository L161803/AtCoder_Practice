def check(): 
    # 全ての条件における範囲が1以下に収まっているかどうか
    # すべてのuiとl(i+1)の差がabs(t(i+1)-t(i))以下
    flag = True

    N, H = map(int, input().split())
    current_time = 0
    min_h = H
    max_h = H

    for _ in range(N):
        t, l, u = map(int, input().split())
        if not flag: continue

        dt = t-current_time

        min_reach = min_h - dt
        max_reach = max_h + dt

        next_min_reach = max(min_reach, l)
        next_max_reach = min(max_reach, u)

        if next_min_reach > next_max_reach:
            flag = False
        else:
            min_h = next_min_reach
            max_h = next_max_reach
            current_time = t

    if flag:print("Yes")
    else:   print("No")

T = int(input())
for _ in range(T):
    check()