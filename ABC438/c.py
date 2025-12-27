import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

stack = []

for a in A:
    stack.append(a)

    if len(stack)>=4:
        if stack[-1]==stack[-2]==stack[-3]==stack[-4]:
            del stack[-4:]

print(len(stack))