# ABC085C - Otoshidama
N, Y = map(int, input().split())
y = Y//1000

for i in range(N+1):          # 0..a 枚
    for j in range(N-i+1):      # 0..b 枚
        k = N-j-i
        if 10*i + 5*j+1*k == y:
            print(i,j,k)
            exit()
print(-1,-1,-1)