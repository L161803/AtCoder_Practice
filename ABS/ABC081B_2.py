#ABC081B-Shift only
N = int(input())
s = list(map(int, input().split()))
ans = 0

while True:
    # 1回でも奇数があれば終了
    if any(x%2==1 for x in s):
        print(ans)
        break
    # 全部偶数なら2で割って回数を+1
    s = [x // 2 for x in s]
    ans += 1
