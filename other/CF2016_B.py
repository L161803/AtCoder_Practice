n, a, b = map(int, input().split())
S = input()
tmp = a+b
cnt = 0
i=0
b_rank = 1
while cnt < tmp:
    if S[i]=="c":
        print("No")
        continue
    if S[i]=="a":
        print("yes")
        continue
    if S[i]=="b":
        if b_rank <= b:
            print("Yes")
            b_rank += 1
        else:
            print("No")