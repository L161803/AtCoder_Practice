N, M = map(int, input().split())

if N>M:
    for i in range(M):
        print("OK")
    for i in range(N-M):
        print("Too Many Requests")

elif N<=M:
    for i in range(N):
        print("OK")