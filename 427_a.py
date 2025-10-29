s = list(input())
if len(s)%2==0:
    s.pop((len(s)//2)+1)
else:
    s.pop((len(s)//2))
print("".join(s))