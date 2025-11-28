tmp = [i*j for i in range(1,10) for j in range(1,10)]
N = int(input())

print("Yes" if N in tmp else "No")