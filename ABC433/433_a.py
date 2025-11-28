X, Y, Z = map(int, input().split())

for _ in range(100):
    if (X // Y) == Z:
        print("Yes")
        break
    else:
        X += 1
        Y += 1