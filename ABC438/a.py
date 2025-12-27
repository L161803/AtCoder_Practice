import sys
input = sys.stdin.readline
d, f = map(int, input().split())

for i in range(100):
    if (f+7*i) > d:
        print(f+7*i-d)
        break