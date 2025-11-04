#ABC087B - Coins
#26ms
a = int(input())  # 500円
b = int(input())  # 100円
c = int(input())  # 50円
x = int(input())  # 合計

ans = 0
for i in range(a + 1):          # 0..a 枚
    for j in range(b + 1):      # 0..b 枚
        for k in range(c + 1):  # 0..c 枚
            if 500*i + 100*j + 50*k == x:
                ans += 1
print(ans)

#11ms
for i in range(a+1):
    rem1 = x - 500*i
    if rem1<0:
        break
    for j in range(b+1):
        rem2 = rem1 - 100*j
        if rem2<0:
            break

        if rem2%50 == 0 and rem2//50<=c:
            ans += 1