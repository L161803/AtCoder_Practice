N = int(input())
a=[]

for i in range(N+1):
    x = i
    if i==0:
        a.append(1)
        continue
    else:
        while x:
            tmp = x%10
            x = x//10

    a.append(a[i-1]+tmp)

print(sum(a))