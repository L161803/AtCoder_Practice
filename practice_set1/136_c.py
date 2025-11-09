# ABC136C - Build Stairs
# 想定：高々要素e10個の配列なので、純粋にループ回してもよさそう
# 　　：ある添え字iより大きい添え字の要素が小さすぎたら単調非減少を作れない
# 実装：毎回添え字i以上の要素から最小を保存していると計算量が爆発する
# 対策：下からループを回して、i-1が最大ならneedを更新
# 計算：１回の走査O(N)

N = int(input())
h = list(map(int, input().split()))
need = 0
for i in h:
    if i < need:
        print("No")
        exit()
    need = max(need,i-1)
else:
    print("Yes")