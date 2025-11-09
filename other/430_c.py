N,A,B = map(int,input().split())
s = list(input())

def start(i,A,B):
    acnt = 0
    bcnt = 0
    check = 0
    while True:
        for j in range(i+1,N):
            if s[j] == "a":
                acnt += 1
            elif s[j] == "b":
                bcnt += 1

        if acnt == A:
            return check
        elif bcnt == B:
            return check
        
        check += 1
            
        
 

for i in range(len(s)):
    print(start(i, A, B))

