import sys
input = sys.stdin.readline

N = int(input())
B = list(map(int, input().split()))

class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & (-i)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

bit_left = BIT(N)
left_counts = [0] * N
    
for i in range(N):
    val = B[i]
    count = bit_left.sum(val)
    bit_left.add(val, 1)
    left_counts[i] = bit_left.sum(val)

bit_right = BIT(N)
right_counts = [0] * N
    
for i in range(N - 1, -1, -1):
    val = B[i]
    bit_right.add(val, 1)
    right_counts[i] = bit_right.sum(val)

ans = 0
for i in range(N):
    ans += left_counts[i] * right_counts[i]

print(ans)
