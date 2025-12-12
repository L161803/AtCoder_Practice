N = int(input())
A = list(map(int,input().split()))
ans = 0

for l in range(N):
    for r in range(l,N):

        current_sum = sum(A[l:r+1])

        flag = True

        for i in range(l,r+1):
            if current_sum % A[i] == 0:
                flag = False
                break
            
        if flag:
            ans += 1

print(ans)