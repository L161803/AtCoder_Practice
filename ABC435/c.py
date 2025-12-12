N = int(input())
A = list(map(int, input().split()))
ans = 1
reach = 1 + A[0]

for i in range(2,N+1):
    if i<reach:
        ans += 1

        new_reach = i + A[i-1]

        if new_reach > reach:
            reach = new_reach

    else:
        break

print(ans)