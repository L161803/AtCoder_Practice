#想定：なんとなく見覚えがあるな、程度。
#　　　解法は全く見当がつかない
#実際：手つかず

from itertools import accumulate    #累積和
import bisect   #二分探索

N, A, B = list(map(int, input().split()))
S = input()

#累積和の考えを使う
#【Sのl文字目からr文字目までにaは何個含まれるか】
#Sのi文字目までに含まれるaの個数をX_iとすると
#Sのl文字目からr文字目までに含まれるaの個数はXr-X_(l-1)としてO(1)
a = [1 if i == "a" else 0 for i in S]   #aのインデックスリスト
AS = [0] + list(accumulate(a)) #累積和
b = [1 if i == "b" else 0 for i in S]   #bのインデックスリスト
BS = [0] + list(accumulate(b)) #累積和

ans = 0
for i in range(N):
    #aについての条件を満たす最小のindex
    left = bisect.bisect_left(AS, AS[i]+A)
    #bについての条件を満たす最小のindex
    right = bisect.bisect_left(BS, BS[i]+B)
    #それぞれの条件で処理
    ans += max(0, right-left)
print(ans)

#code from makimakimakki
#課題：二分探索、累積和の使い方をマスターする