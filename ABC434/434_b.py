N, M = map(int, input().split())

sum_sizes = [0] * (M + 1)
counts = [0] * (M + 1)

for _ in range(N):
    a, b = map(int, input().split())
    
    sum_sizes[a] += b
    
    counts[a] += 1

for k in range(1, M + 1):
    ans = sum_sizes[k] / counts[k]
    print(ans)