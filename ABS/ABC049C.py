# ABC049C - Daydream
S = input()

# 末尾一致で長い方を先に削る
while S:
    if   S.endswith("dreamer"): S = S[:-7]
    elif S.endswith("eraser"):  S = S[:-6]
    elif S.endswith("dream"):   S = S[:-5]
    elif S.endswith("erase"):   S = S[:-5]
    else:
        print("NO")
        break
else:
    print("YES")