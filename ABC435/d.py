import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N, M = map(int, input().split())


relation_rev = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    relation_rev[v].append(u)

Q = int(input())

black_root = set()
queue = deque()

for _ in range(Q):
    line = list(map(int, input().split()))
    q_type = line[0]
    node = line[1]

    if q_type == 1:
        if node in black_root:
            continue
            
        black_root.add(node)
        queue.append(node)

        while queue:
            curr = queue.popleft()

            for p in relation_rev[curr]:
                if p not in black_root:
                    black_root.add(p)
                    queue.append(p)

    elif q_type == 2:
        if node in black_root:
            print("Yes")
        else:
            print("No")
    