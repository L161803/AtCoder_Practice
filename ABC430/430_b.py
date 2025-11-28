#DATE: 11-02-2025
#ABC430
#B:  Count Subgrid

#二次元配列の部分配列のパターン数を取得する
#想定：何とか行ごとに切り出せばパターンを処理できないかと考えた
#実際：collectionsのCounterなどで各要素の比較を行ったが、
#    　標準ライブラリでなんとかできたし、
# 　　　計算量が少ないのでサボらなければACになる

#input
N, M = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())

#後程使う
ptn = set()

#スライスするときにindex errorを吐かないために丁寧にループ
for i in range(N-M+1):
    for j in range(N-M+1):

        tmp=[]

        #スライスする部分
        for k in range(M):
            slice = S[i+k][j:j+M]
            tmp.append(slice)
        
        #set()にlist型は入らないのでtuple化する
        pattern_tuple = tuple(tmp)

        ptn.add(pattern_tuple)

#重複を消した要素数を出力
print(len(ptn))