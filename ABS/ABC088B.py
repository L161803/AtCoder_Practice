#ABC088B - Card Game for Two
N = int(input())
A = sorted(map(int, input().split()), reverse=True)
Alice = sum(A[i] for i in range(0, len(A), 2))
Bob = sum(A[i] for i in range(1, len(A),2))
print(Alice-Bob)

#改善
print(sum(A[::2])-sum(A[1::2]))