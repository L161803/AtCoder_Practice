X=sorted(list(input()))
for i in X:
    if i!="0":
        tmp = i
        X.remove(i)
        break
ans = tmp+"".join(X)
print(int(ans))
