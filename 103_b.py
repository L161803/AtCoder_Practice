from collections import deque, Counter

s=list(input())
t=list(input())
dq = deque(s)

ans = "No"
i=0
while i<len(s):
    if list(dq)==t:
        ans = "Yes"
        break
    else:
        dq.rotate(1)
        i += 1

print(ans)