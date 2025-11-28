N = int(input())
A = list(map(int, input().split()))

for i in range(len(A)):
    idx = -1

    for j in range(i-1, -1, -1):
        if A[j] > A[i]:
            idx = j
    
    print(idx)


