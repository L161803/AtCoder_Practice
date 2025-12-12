def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    if len(set(X)) != N or len(set(Y)) != M:
        print("No")
        return

    if max(X) != max(Y):
        print("No")
        return

    grid = [[-1] * M for _ in range(N)]
    
    set_X = set(X)
    set_Y = set(Y)
    
    idx_X = {val: i for i, val in enumerate(X)}
    idx_Y = {val: j for j, val in enumerate(Y)}
    
    max_val = max(X)
    i_max = idx_X[max_val]
    j_max = idx_Y[max_val]
    
    for val in X:
        i = idx_X[val]
        if val in set_Y:
            j = idx_Y[val]
            grid[i][j] = val
        else:
            grid[i][j_max] = val
            
    for val in Y:
        j = idx_Y[val]
        if val in set_X:
            continue
        else:
            grid[i_max][j] = val

    used_values = set(X) | set(Y)
    
    # 未使用の数字リストを作成（小さい順）
    # 全体で N*M 個、そこから使った分を除く
    unused = []
    # N*M が大きい場合、このリスト作成は工夫が必要だが、
    # 制約 N*M <= 2*10^5 なので単純なループでOK
    current_v = 1
    sorted_used = sorted(list(used_values))
    used_idx = 0
    
    # 効率的に unused を生成するジェネレータ的アプローチ
    # または単純にリスト作成
    # ここではわかりやすくリストを作る
    all_needed = []
    ptr = 0
    for v in range(1, N * M + 1):
        if ptr < len(sorted_used) and v == sorted_used[ptr]:
            ptr += 1
        else:
            all_needed.append(v)
            
    unused_iter = iter(all_needed)
    
    # グリッドの空きマスを埋める
    for i in range(N):
        for j in range(M):
            if grid[i][j] == -1:
                try:
                    fill_val = next(unused_iter)
                except StopIteration:
                    # 理論上ここには来ないはず
                    print("No")
                    return
                
                # 制約チェック：そのマスの行最大値・列最大値を超えてはいけない
                if fill_val > min(X[i], Y[j]):
                    print("No")
                    return
                
                grid[i][j] = fill_val

    # 5. 出力
    print("Yes")
    for row in grid:
        print(*row)

# 入力のTケース
T_cases = int(input())
exit()

# 入力形式に合わせてパースするヘルパーが必要ですが、
# 上記の solve 関数は単発用です。
# 実際の提出時は以下のようにまとめて処理します。

def run():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    iterator = iter(input_data)
    try:
        T = int(next(iterator))
    except StopIteration:
        return
        
    for _ in range(T):
        N = int(next(iterator))
        M = int(next(iterator))
        X = []
        for _ in range(N):
            X.append(int(next(iterator)))
        Y = []
        for _ in range(M):
            Y.append(int(next(iterator)))
            
        # ここにロジックを展開（関数呼び出しだと変数スコープが楽）
        solve_case(N, M, X, Y)

def solve_case(N, M, X, Y):
    # (上記のロジックと同じ内容)
    if len(set(X)) != N or len(set(Y)) != M:
        print("No"); return
    if max(X) != max(Y):
        print("No"); return

    grid = [[-1] * M for _ in range(N)]
    set_Y = set(Y)
    idx_X = {x: i for i, x in enumerate(X)}
    idx_Y = {y: i for i, y in enumerate(Y)}
    
    max_val = max(X)
    i_max = idx_X[max_val]
    j_max = idx_Y[max_val]
    
    # 配置
    for x in X:
        r = idx_X[x]
        if x in set_Y:
            c = idx_Y[x]
            grid[r][c] = x
        else:
            grid[r][j_max] = x
            
    for y in Y:
        if y not in idx_X: # idx_X is simpler check than set_X
            c = idx_Y[y]
            grid[i_max][c] = y
            
    # 未使用数字の準備
    used = set(X) | set(Y)
    # N*Mまでの数字でusedに入っていないものを生成
    # 効率化: N*M <= 2*10^5 なので、全探索でOK
    
    fillers = []
    # ここはボトルネックになりうるので注意
    # しかし sum(NM) <= 2*10^5 なので、毎回作っても間に合う
    
    # 高速化のため、現在の未使用最小値を管理する方針でも良いが、リスト作成で十分
    is_used = [False] * (N * M + 1)
    for u in used:
        is_used[u] = True
    
    fillers = [i for i in range(1, N * M + 1) if not is_used[i]]
    fillers_iter = iter(fillers)
    
    for r in range(N):
        for c in range(M):
            if grid[r][c] == -1:
                try:
                    val = next(fillers_iter)
                except StopIteration:
                    print("No"); return
                
                if val > X[r] or val > Y[c]: # min(X[r], Y[c]) と同じ意味
                    print("No"); return
                grid[r][c] = val
                
    print("Yes")
    for row in grid:
        print(*(row))

if __name__ == '__main__':
    run()