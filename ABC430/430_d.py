#ABC430-D-Neighbor Distance
#想定：座標kに一人追加された時に変化が生じるのは
#　　　k-1, k, k+1の三つだけなので、それを更新して和を考える
#　　　実装くそ重そう

#CODE from seigot33
from sortedcontainers import SortedList

def solve():
    N = int(input())
    X = list(map(int, input().split()))

    # ソート済みリスト（平行二分探索木）
    positions = SortedList([0])

    # 各座標の最近傍距離を保持
    min_distances = {}

    total_sum = 0 # 初期状態の総和（人0だけの場合は0としてスタート）

    for i in range(N):
        xi = X[i]

        # 挿入位置のインデックスを取得
        idx = positions.bisect_left(xi)

        # 新しい人の最近傍距離を計算
        new_min_dist = float('inf')

        left_pos = None
        if idx > 0:
            left_pos = positions[idx-1]
            dist_to_left = xi-left_pos
            new_min_dist = min(new_min_dist, dist_to_left)

            # 左隣の人の最近傍距離を更新
            if left_pos in min_distances:
                total_sum -= min_distances[left_pos]

            # 左隣の新しい最近傍距離を計算
            new_dist_for_left = dist_to_left
            if idx > 1:
                new_dist_for_left = min(new_dist_for_left, left_pos-positions[idx-2])

            min_distances[left_pos] = new_dist_for_left
            total_sum += new_dist_for_left

        # 右隣が存在する場合
        right_pos = None
        if idx < len(positions):
            right_pos = positions[idx]
            dist_to_right = right_pos - xi
            new_min_dist = min(new_min_dist, dist_to_right)

            # 右隣の人の最近傍距離を更新
            if right_pos in min_distances:
                total_sum -= min_distances[right_pos]

            # 右隣の新しい最近傍距離を計算
            new_dist_for_right = dist_to_right
            if idx+1 < len(positions):
                new_dist_for_right = min(new_dist_for_right, positions[idx+1]-right_pos)
                
            min_distances[right_pos] = new_dist_for_right
            total_sum += new_dist_for_right

        positions.add(xi)
        min_distances[xi] = new_min_dist
        total_sum += new_min_dist

        print(total_sum)

solve()

# 感想　　　　：やべぇ！
# 感想（本筋）：挿入位置を二分探索で求めることが最初の計算量を減らす工夫に感動した。
# 　　　　　　：確かに、一回消して計算しなおして戻せば更新できる。

# 課題　　　　：二分探索とsortedcontainersについて理解を深める