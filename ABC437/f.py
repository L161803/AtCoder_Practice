import sys
input = sys.stdin.read

data = input().split()
iterator = iter(data)

N = int(next(iterator))
Q = int(next(iterator))

size = 1
while size < N:
    size *= 2
    
INF = 10**18

tree_max_s = [-INF] * (2 * size)
tree_min_s = [INF] * (2 * size)
tree_max_d = [-INF] * (2 * size)
tree_min_d = [INF] * (2 * size)

for i in range(N):
    X = int(next(iterator))
    Y = int(next(iterator))

    idx = size + i
    s = X + Y
    d = X - Y

    tree_max_s[idx] = s
    tree_min_s[idx] = s
    tree_max_d[idx] = d
    tree_min_d[idx] = d

for i in range(size - 1, 0, -1):
    l = 2 * i
    r = 2 * i + 1
    tree_max_s[i] = max(tree_max_s[l], tree_max_s[r])
    tree_min_s[i] = min(tree_min_s[l], tree_min_s[r])
    tree_max_d[i] = max(tree_max_d[l], tree_max_d[r])
    tree_min_d[i] = min(tree_min_d[l], tree_min_d[r])

output = []


for _ in range(Q):
    type = int(next(iterator))
        
    if type == 1:
        i = int(next(iterator)) - 1 
        x = int(next(iterator))
        y = int(next(iterator))
            
        idx = size + i
        s = x + y
        d = x - y
        
        tree_max_s[idx] = s
        tree_min_s[idx] = s
        tree_max_d[idx] = d
        tree_min_d[idx] = d
            
        idx //= 2
        
        while idx > 0:
            l = 2 * idx
            r = 2 * idx + 1
            tree_max_s[idx] = max(tree_max_s[l], tree_max_s[r])
            tree_min_s[idx] = min(tree_min_s[l], tree_min_s[r])
            tree_max_d[idx] = max(tree_max_d[l], tree_max_d[r])
            tree_min_d[idx] = min(tree_min_d[l], tree_min_d[r])
            idx //= 2
                
    else:
        L = int(next(iterator)) - 1
        R = int(next(iterator)) 
        x = int(next(iterator))
        y = int(next(iterator))
            
        l_idx = size + L
        r_idx = size + R
            
        cur_max_s = -INF
        cur_min_s = INF
        cur_max_d = -INF
        cur_min_d = INF
            
        while l_idx < r_idx:
            if l_idx % 2 == 1:
                cur_max_s = max(cur_max_s, tree_max_s[l_idx])
                cur_min_s = min(cur_min_s, tree_min_s[l_idx])
                cur_max_d = max(cur_max_d, tree_max_d[l_idx])
                cur_min_d = min(cur_min_d, tree_min_d[l_idx])
                l_idx += 1
            if r_idx % 2 == 1:
                r_idx -= 1
                cur_max_s = max(cur_max_s, tree_max_s[r_idx])
                cur_min_s = min(cur_min_s, tree_min_s[r_idx])
                cur_max_d = max(cur_max_d, tree_max_d[r_idx])
                cur_min_d = min(cur_min_d, tree_min_d[r_idx])
                
            l_idx //= 2
            r_idx //= 2
            
        ans = max(
            cur_max_s - (x + y),
            cur_max_d - (x - y),
            (x - y) - cur_min_d,
            (x + y) - cur_min_s
        )

        output.append(str(ans))
            
print('\n'.join(output))