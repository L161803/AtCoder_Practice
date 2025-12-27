import sys
input = sys.stdin.readline

n,q = map(int, input().split())
A = [0] + list(map(int, input().split()))

queries = []

for i in range(q):
    t,b = map(int, input().split())
    queries.append((t,b))

next_pos=[[0]*(n+1) for _ in range(30)]
total_water=[[0]*(n+1) for _ in range(30)]

for i in range(1,n+1):
    next_pos[0][i]=A[i]
    total_water[0][i]=i

for k in range(29):
    for i in range(1,n+1):
        mid = next_pos[k][i]
        next_pos[k+1][i]=next_pos[k][mid]
        total_water[k+1][i]=total_water[k][i]+total_water[k][mid]

for t,b in queries:
    curr_pos=b
    curr_water=0

    for k in range(30):
        if (t>>k)&1:
            curr_water += total_water[k][curr_pos]
            curr_pos = next_pos[k][curr_pos]

    print(curr_water)