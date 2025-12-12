S = list(input())
T = []
for i in range(len(S)):
    if S[i]=="#":T.append("#")
    elif "." not in T: T.append(".")
    else:T.append("o")

print("".join(T))