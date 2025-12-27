import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())
adj = [[] for _ in range(N + 1)]
    
for i in range(1, N + 1):
    x, y = map(int, input().split())
    adj[x].append((y, i))

ans = []
    

def dfs(current_nodes):
    
    for u in current_nodes:
        if u != 0:
            ans.append(u)
        
    all_edges = []
    for u in current_nodes:
        for w, v in adj[u]:
            all_edges.append((w, v))
        
    if not all_edges:
        return
    
    all_edges.sort()

    n_edges = len(all_edges)
    start = 0

    while start < n_edges:
        w = all_edges[start][0]
        end = start + 1
        while end < n_edges and all_edges[end][0] == w:
            end += 1
        nextg = [e[1] for e in all_edges[start:end]]
        dfs(nextg)
        start = end

dfs([0])
    
print(*(ans))

